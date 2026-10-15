from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def project_costing():
    if request.method == "POST":
        # Get form data
        try:
            budget = float(request.form["budget"])
            labor_pct = float(request.form["labor"])
            material_pct = float(request.form["materials"])
            equipment_pct = float(request.form["equipment"])
            contingency_pct = float(request.form["contingency"])
        except ValueError:
            return render_template("index.html", error="⚠️ Invalid input. Please enter numbers only.")

        total_pct = labor_pct + material_pct + equipment_pct + contingency_pct
        if total_pct != 100:
            return render_template("index.html", error=f"⚠️ Total percentage must be 100%. You entered {total_pct}%.")

        # Compute costs
        labor_cost = (labor_pct / 100) * budget
        material_cost = (material_pct / 100) * budget
        equipment_cost = (equipment_pct / 100) * budget
        contingency_cost = (contingency_pct / 100) * budget
        total_cost = labor_cost + material_cost + equipment_cost + contingency_cost

        remaining_budget = budget - total_cost

        return render_template(
            "result.html",
            budget=budget,
            labor_cost=labor_cost,
            material_cost=material_cost,
            equipment_cost=equipment_cost,
            contingency_cost=contingency_cost,
            total_cost=total_cost,
            remaining_budget=remaining_budget
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
