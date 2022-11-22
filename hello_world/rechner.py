from flask import Flask
from flask import request
from flask import render_template

app = Flask("Rechner")

@app.route('/test')
def test():
    return render_template("pretty_rechner.html")


@app.route('/add', methods=["GET", "POST"])
def add():
    print(f'Method: {request.method}')
    if request.method == "GET":
        return render_template("rechner.html")

    if request.method == "POST":
        print(f'Method{request.form}')
        ergebnis = int(request.form['zahl_0']) + int(request.form['zahl_1'])

        return render_template("rechner.html", ergebnis=ergebnis)

  #  ergebnis = int(zahl_0) + int(zahl_1)
  #  msg = f"Das Ergebnis ist {ergebnis}!"
    return "Irgendwas ist falsch"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
