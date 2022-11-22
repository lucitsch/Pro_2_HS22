from flask import Flask
from flask import render_template

import random
app = Flask("Hello WOrld")

@app.route('/greet_all')
def greet_all():
    auswahl = ["Fabian", "Markus", "Franz", "Armando"]
    return render_template('hello_all.html', alle_namen=auswahl)


@app.route('/hello')
def hello_world():
    auswahl = ["Fabian", "Markus", "Franz", "Armando"]
    ausgewaehlter_name = random.choice(auswahl)
    return render_template('hello.html', name=ausgewaehlter_name)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

