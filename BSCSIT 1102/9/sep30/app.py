from flask import Flask, render_template, request
import math

app = Flask(__name__)

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
    return render_template("index.html")

@app.route("/temperature", methods=["POST"])
def temperature():
    try:
        celsius = float(request.form.get("celsius", 0))
        fahrenheit = float(request.form.get("fahrenheit", 0))
        celsius_result = fahrenheit_to_celsius(fahrenheit)
        fahrenheit_result = celsius_to_fahrenheit(celsius)
        return render_template(
            "result.html",
            celsius=celsius,
            fahrenheit=fahrenheit,
            celsius_result=celsius_result,
            fahrenheit_result=fahrenheit_result,
            grades=None,
            primes=None
        )
    except ValueError:
        return render_template("index.html", error="⚠️ Invalid input. Please enter numbers for temperature.")

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
        grades=high_grades,
        primes=None
    )

@app.route("/primes", methods=["POST"])
def primes():
    try:
        N = int(request.form.get("N", 0))
        if N < 2:
            return render_template("index.html", error="⚠️ Please enter a number greater than or equal to 2.")
        prime_numbers = prime_list(N)
        return render_template(
            "result.html",
            celsius=None,
            fahrenheit=None,
            grades=None,
            primes=prime_numbers,
            N=N
        )
    except ValueError:
        return render_template("index.html", error="⚠️ Invalid input. Please enter a valid number for N.")

if __name__ == "__main__":
 app.run(debug=True, port=0)