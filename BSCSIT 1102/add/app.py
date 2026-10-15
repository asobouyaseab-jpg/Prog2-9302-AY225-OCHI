from flask import Flask, render_template, request, session
import math

app = Flask(__name__)
app.secret_key = "your-secret-key"  # セッション用キー（履歴保存に使用）

# 変換モード（デフォルトは摂氏→華氏）
conversion_mode = "CtoF"  # CtoF: 摂氏→華氏, FtoC: 華氏→摂氏

# Temperature Conversion Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Prime Number Functions
def _prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(N):
    return [n for n in range(2, N + 1) if _prime(n)]

@app.route("/", methods=["GET", "POST"])
def index():
    global conversion_mode
    error = None

    if request.method == "POST":
        if "toggle" in request.form:
            # 単位切り替えボタン
            conversion_mode = "FtoC" if conversion_mode == "CtoF" else "CtoF"

    # 温度変換の入力ラベル
    input_label = "摂氏 (°C)" if conversion_mode == "CtoF" else "華氏 (°F)"
    output_label = "華氏 (°F)" if conversion_mode == "CtoF" else "摂氏 (°C)"

    return render_template("index.html", input_label=input_label, output_label=output_label, error=error)

@app.route("/temperature", methods=["POST"])
def temperature():
    global conversion_mode
    try:
        temp = request.form.get("temperature")
        if not temp:
            raise ValueError("温度を入力してください。")
        temp = float(temp)
        if conversion_mode == "CtoF":
            # 摂氏から華氏へ
            result = celsius_to_fahrenheit(temp)
            result_str = f"{temp:.2f} °C → {result:.2f} °F"
            result_display = f"{result:.2f} °F"
            input_unit = "摂氏 (°C)"
        else:
            # 華氏から摂氏へ
            result = fahrenheit_to_celsius(temp)
            result_str = f"{temp:.2f} °F → {result:.2f} °C"
            result_display = f"{result:.2f} °C"
            input_unit = "華氏 (°F)"

        # 履歴に追加（セッション使用）
        history = session.get("history", [])
        history.append(result_str)
        session["history"] = history[-5:]  # 最新5件のみ保存

        return render_template(
            "result.html",
            celsius=None if conversion_mode != "CtoF" else temp,
            fahrenheit=None if conversion_mode != "FtoC" else temp,
            celsius_result=None if conversion_mode != "FtoC" else result,
            fahrenheit_result=None if conversion_mode != "CtoF" else result,
            result_display=result_display,
            input_unit=input_unit,
            grades=None,
            primes=None,
            history=session.get("history", []),
            error=None
        )
    except ValueError as e:
        return render_template("index.html", error=f"⚠️ 無効な入力です：{str(e)}", input_label="摂氏 (°C)", output_label="華氏 (°F)")

@app.route("/grades", methods=["POST"])
def grades():
    grades = {
        "Arnold": 90,
        "Dwein": 83,
        "Randy": 88,
        "Seagal": 78,
        "Statham": 93
    }
    high_grades = {k: v for k, v in grades.items() if v >= 85}
    return render_template(
        "result.html",
        celsius=None,
        fahrenheit=None,
        celsius_result=None,
        fahrenheit_result=None,
        result_display=None,
        input_unit=None,
        grades=high_grades,
        primes=None,
        history=session.get("history", []),
        error=None
    )

@app.route("/primes", methods=["POST"])
def primes():
    try:
        N = int(request.form.get("N", 0))
        if N < 2:
            return render_template("index.html", error="⚠️ 2以上の数を入力してください。", input_label="摂氏 (°C)", output_label="華氏 (°F)")
        prime_numbers = prime_list(N)
        return render_template(
            "result.html",
            celsius=None,
            fahrenheit=None,
            celsius_result=None,
            fahrenheit_result=None,
            result_display=None,
            input_unit=None,
            grades=None,
            primes=prime_numbers,
            N=N,
            history=session.get("history", []),
            error=None
        )
    except ValueError:
        return render_template("index.html", error="⚠️ 無効な入力です。数値を入力してください。", input_label="摂氏 (°C)", output_label="華氏 (°F)")

@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["history"] = []
    return render_template("index.html", input_label="摂氏 (°C)", output_label="華氏 (°F)", error=None)

if __name__ == "__main__":
    app.run(debug=False, port=5001)  # ポート5001で実行（競合回避）