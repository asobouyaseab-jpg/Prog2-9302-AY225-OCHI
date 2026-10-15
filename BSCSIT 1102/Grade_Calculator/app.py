from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def grade_calculator():
    error = None
    result = None

    if request.method == "POST":
        try:
            # Get and validate inputs
            prelim_grade = request.form.get("prelim_grade", type=float)
            absences = request.form.get("absences", type=int)

            if prelim_grade is None or absences is None:
                error = "Please enter valid numbers"
            elif prelim_grade < 0 or prelim_grade > 100:
                error = "Preliminary grade must be between 0 and 100"
            elif absences < 0:
                error = "Absences cannot be negative"
            else:
                # Calculate status and required grades
                # Assuming equal weight for prelim, midterm, and final (1/3 each)
                current_total = prelim_grade / 3
                required_total_pass = 75 - current_total  # For passing (75%)
                required_total_deans = 90 - current_total  # For Dean's List (90%)

                # Calculate required midterm and final grades
                # Each remaining term (midterm and final) contributes 1/3, so multiply by 3/2 to get individual grade
                required_midterm_pass = max(0, min(100, required_total_pass * 3 / 2))
                required_final_pass = max(0, min(100, required_total_pass * 3 / 2))
                required_midterm_deans = max(0, min(100, required_total_deans * 3 / 2))
                required_final_deans = max(0, min(100, required_total_deans * 3 / 2))

                # Create result dictionary
                result = {
                    'prelim_grade': round(prelim_grade, 2),
                    'absences': absences,
                    'passed': prelim_grade >= 75 and absences <= 3,  # Assuming max 3 absences allowed
                    'deans_list': prelim_grade >= 90 and absences == 0,
                    'required_midterm_pass': round(required_midterm_pass, 2),
                    'required_final_pass': round(required_final_pass, 2),
                    'required_midterm_deans': round(required_midterm_deans, 2),
                    'required_final_deans': round(required_final_deans, 2),
                }

        except (ValueError, TypeError):
            error = "Please enter valid numbers"

    return render_template("index.html", error=error, result=result)

if __name__ == "__main__":
    app.run(debug=True)