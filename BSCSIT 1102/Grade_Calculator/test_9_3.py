from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Grade Calculator</title>
    <style>
       body {font-family: Arial; text-align: center; margin-top: 50px;}
       .error{color:red;}
       .success{color:green;}
       .result{margin-top: 20px;padding:10px;border: 1px solid #ccc;}
     </style>
</head>
<body>
    <h1>Grade Calculator</h1>
    <form method="POST">
        <input type="number" name="prelim_grade" placeholder="Enter Preliminary Grade(0-100)" step="0.01" required>
        <input type="number" name="absences" placeholder="Enter Number of Absences" step="1" required>
        <button type="submit">Calculate</button>
    </form>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

    {% if result is not none %}
        <div class="result">
        <h2>Results</h2>
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
         <p>To Pass (75%): Need {{ result.required_final_pass }} in Final </p>
         <p>For Dean's List (90%): Need {{ result.required_final_deans }} in Final </p>
         </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def grade_calculator():
    error = None
    result = None

    if request.method == "POST":
        try:
            # Get and validate inputs
            prelim_grade = request.form.get("prelim_grade", type=float)
            absences = request.form.get("absences", type=int)
    
            if prelim_grade < 0 or prelim_grade > 100:
                error = "Preliminary grade must be between 0 and 100"
            elif absences < 0:
                error = "Absences cannot be negative"
            else:
                # Calculate status and required grades
                # Assuming equal weight for prelim, midterm, and final (1/3 each)
                current_total = prelim_grade / 3
                required_total_pass = 75 - current_total  # For passing (75%)
                required_total_deans = 90 - current_total  # For Dean's list (90%)

                # Calculate required average for remaining 2/3 (midterm + final)
                avg_remaining_pass = required_total_pass / (2 / 3)
                avg_remaining_deans = required_total_deans / (2 / 3)

                # Since midterm and final have equal weight, each needs the avg_remaining
                required_midterm_pass = avg_remaining_pass
                required_final_pass = avg_remaining_pass
                required_midterm_deans = avg_remaining_deans
                required_final_deans = avg_remaining_deans

                # Clamp to 0-100 range
                required_midterm_pass = max(min(required_midterm_pass, 100), 0)
                required_final_pass = max(min(required_final_pass, 100), 0)
                required_midterm_deans = max(min(required_midterm_deans, 100), 0)
                required_final_deans = max(min(required_final_deans, 100), 0)

                # Create result dictionary
                result = {
                    'prelim_grade': round(prelim_grade, 2),
                    'absences': absences,
                    'passed': prelim_grade >= 75 and absences <= 3,  # Assuming max 3 absences allowed
                    'deans_list': prelim_grade >= 90 and absences <= 0,
                    'required_midterm_pass': round(required_midterm_pass, 2),
                    'required_midterm_deans': round(required_midterm_deans, 2),
                    'required_final_pass': round(required_final_pass, 2),
                    'required_final_deans': round(required_final_deans, 2),
                }
        except (ValueError, TypeError):
            error = "Please enter valid numbers"

    return render_template_string(html_template, error=error, result=result)


if __name__ == "__main__":
    app.run(debug=True)