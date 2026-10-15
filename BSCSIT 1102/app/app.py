from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template inside Python using render_template_string
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Add Two Numbers</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1>Add Two Numbers</h1>
    <form method="POST">
        <input type="number" name="num1" placeholder="Enter first number" required>
        <input type="number" name="num2" placeholder="Enter second number" required>
        <button type="submit">Add</button>
    </form>

    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def add_numbers():
    result = None
    if request.method == "POST":
        num1 = request.form.get("num1", type=float)
        num2 = request.form.get("num2", type=float)
        result = num1 + num2
    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    app.run(debug=True)