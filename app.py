from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        rent = int(request.form["rent"])
        food = int(request.form["food"])
        electricity_spend = int(request.form["electricity_spend"])
        charge_per_unit = int(request.form["charge_per_unit"])
        persons = int(request.form["persons"])

        total_bill = electricity_spend * charge_per_unit
        output = (food + rent + total_bill) // persons

        return render_template("index.html", output=output)

    return render_template("index.html", output=None)

if __name__ == "__main__":
    app.run(debug=True)
