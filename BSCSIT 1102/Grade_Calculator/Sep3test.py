from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTMLテンプレートをPythonの文字列変数として定義（これで適用可能）
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Grade Calculater</title>
    <style>
        body {font-family: Arial; text-align: center; margin-top: 50px;}
        .error {color: red;}
        .success {color: green;}
        .result {margin-top: 20px; padding: 10px; border: 1px solid #ccc;}
    </style>
</head>
<body>
    <h1>Grade Calculater</h1>
    <form method="POST">
        <input type="number" name="prelim_grade" placeholder="Enter Preliminary Grade(0-100)" step="0.01" required><br><br>
        <input type="number" name="absences" placeholder="Enter Number of Absences" step="1" required><br><br>
        <button type="submit">Calculate</button>
    </form>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

    {% if result is not none %}
        <div class="result">
            <h2>Results: {{ result.prelim_grade }}</h2>
            <p>Preliminary Grade: {{ result.prelim_grade }}</p>
            <p>Absences: {{ result.absences }}</p>
            <p>Status: 
                {% if result.passed %}
                    <span class="success">Passed</span>
                {% else %}
                    <span class="error">Failed</span>
                {% endif %}
            </p>
            <h3>Required Grades</h3>
            <p>To Pass (75%): Need {{ result.required_final_pass }} in Final</p>
            <p>For Dean's List (90%): Need {{ result.required_final_deans }} in Final</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def grade_calculater():
     error = None
     result = None

     if request.method == "POST":
        try:
            # 入力の取得と検証をtry内で正しく行う
            prelim_grade = float(request.form.get("prelim_grade", 0))
            absences = int(request.form.get("absences", 0))

            if prelim_grade < 0 or prelim_grade > 100:
                error = "Preliminary grade must be between 0 and 100"
            elif absences < 0:
                error = "Absences cannot be negative"
            else:
                # 計算（Prelim: 1/3, Midterm: 1/3, Final: 1/3 と仮定）
                current_total = prelim_grade / 3
                required_total_pass = 75 - current_total  # 残り2/3で必要な合計
                required_total_deans = 90 - current_total

                # 残り2/3で必要な合計を各1/3に分配（midtermとfinalが同等と仮定）
                required_each_pass = required_total_pass / 2
                required_each_deans = required_total_deans / 2

                # 0-100の範囲にクランプ
                required_final_pass = max(0, min(100, required_each_pass))
                required_final_deans = max(0, min(100, required_each_deans))

                # 結果辞書を作成
                result = {
                    'prelim_grade': round(prelim_grade, 2),
                    'absences': absences,
                    'passed': prelim_grade >= 75 and absences <= 3,  # 仮定: 欠席3回までOK
                    'deans_list': prelim_grade >= 90 and absences <= 0,  # 仮定: 欠席0でディーンズリスト
                    'required_final_pass': round(required_final_pass, 2),
                    'required_final_deans': round(required_final_deans, 2),
                }
        except (ValueError, TypeError):
            error = "Please enter valid numbers"

     return render_template_string(html_template, error=error, result=result)

if __name__ == "__main__":
    app.run(debug=True)