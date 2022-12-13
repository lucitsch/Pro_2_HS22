from flask import Flask
#Flask Paket wird importieren
from flask import render_template
#um die html Datein zu verwenden
from flask import request
from flask import Flask, render_template
from Abschlussprojekt.datenbank import abspeichern, auslesen, packliste_laden
from Abschlussprojekt.sachen_liste import sachen

app = Flask(__name__)


#Starseite
@app.route("/", methods=["GET", "POST"])
def add_new_packliste():
    if request.method == "GET":
        return render_template("index.html", seitentitel="eingabe")

    if request.method == "POST":
        art = request.form['art']
        anzahl = request.form['anzahl']
        deadline = request.form['deadline']
        print(f"Request Form Art: {art}")
        print(f"Request Form Anzahl: {anzahl}")
        print(f"Request Form Deadline: {deadline}")
        abspeichern(art, anzahl, deadline)
        return "hat funktioniert"

@app.route("/packlisten")
def start():
    packliste = packliste_laden()
    return render_template("packliste.html", liste=packliste, seitentitel="start")

#Sommerpackliste
@app.route("/sommerkleider", methods=['GET', 'POST'])
def sommer():
    if request.method == 'POST':
        print(request.form.getlist('mycheckbox'))
        return 'Ihre Auswahl wurde gespeicher. Klicken Sie weiter um Ihre Packliste einzusehen'

    kategorien = ["Sommerbekleidung", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien)

#Winterpackliste
@app.route("/winterkleider", methods=['GET', 'POST'])
def winter():
    if request.method == 'POST':
        print(request.form.getlist('mycheckbox'))
        return 'Ihre Auswahl wurde gespeicher. Klicken Sie weiter um Ihre Packliste einzusehen'

    kategorien = ["Winterkleider", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien)

#Skipackliste
@app.route("/skikleider", methods=['GET', 'POST'])
def ski():
    if request.method == 'POST':
        print(request.form.getlist('mycheckbox'))
        return 'Ihre Auswahl wurde gespeicher. Klicken Sie weiter um Ihre Packliste einzusehen'

    kategorien = ["Skibekleidung", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien)

#Strandkleider
@app.route("/strandkleider", methods=['GET', 'POST'])
def strand():
    if request.method == 'POST':
        print(request.form.getlist('mycheckbox'))
        return 'Ihre Auswahl wurde gespeicher. Klicken Sie weiter um Ihre Packliste einzusehen'

    kategorien = ["Strandbekleidung", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien)


#Ruft Internetseite auf
if __name__ == "__main__":
    app.run(debug=True, port=5007)