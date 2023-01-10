import datetime

from flask import Flask, render_template
from flask import request
from Abschlussprojekt.datenbank import auslesen, abspeichern, packliste_laden, alle_speichern
from Abschlussprojekt.sachen_liste import sachen
from flask import redirect

app = Flask("Packliste")


#Starseite
@app.route("/", methods=["GET", "POST"])
def add_new_packliste():
    if request.method == "GET":
        return render_template("index.html", seitentitel="eingabe")

    if request.method == "POST":
        ort = request.form['ort']
        typ = request.form['typ']
        anzahl = request.form['anzahl']
        deadline = str(datetime.datetime.now())
        print(f"Request From Ort: {ort}")
        print(f"Request Form Typ: {typ}")
        print(f"Request Form Anzahl: {anzahl}")
        print(f"Request Form Deadline: {deadline}")
        abspeichern(ort, typ, anzahl, deadline)
        if typ == "Sommerferien":
            return redirect("/sommerkleider")
        elif typ == "Winterferien":
            return redirect("winterkleider")
        elif typ == "Skiferien":
            return redirect("skikleider")
        elif typ == "Strandferien":
            return redirect("strandkleider")
@app.route("/packlisten", methods=["GET", "POST"])
def start():
    packliste = packliste_laden()
    if request.method == "POST":
        a = request.form.getlist("name")
        print("Deine Packliste wurde gespeichert, du kannst sie in der Datenbank einsehen")
        packliste_last = packliste[-1]
        packliste_last.append(a)
        packliste[-1] = packliste_last
    return render_template("packliste.html", liste=packliste, seitentitel="start")

@app.route("/abrufen", methods=['GET', 'POST'])
def abrufen():
    if request.method == 'POST':
        eintrag = request.form['data']

        return eintrag
#Sommerpackliste
@app.route("/sommerkleider", methods=['GET', 'POST'])
def sommer():
    if request.method == 'POST':
        letzter_eintrag = request.form['letzter_eintrag']
        alle_eintraege = auslesen().split("\n")
        del alle_eintraege[-1]
        name = request.form
        print((list(name)))
        name = name[:-1]
        checks = ";".join(name)
        letzter_eintrag = letzter_eintrag.rstrip(", []")
        letzter_eintrag = letzter_eintrag + "," + str(checks)
        alle_eintraege.append(letzter_eintrag)
        alle_speichern(alle_eintraege)
        return redirect("/packlisten")

    letzter_eintrag = auslesen().split("\n")[-1]
    kategorien = ["Sommerbekleidung", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien, letzter_eintrag=letzter_eintrag)

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

@app.route("/hinzufügen", methods=['GET', 'POST'])
def add_sachen():
    return render_template('Sachen_Hinzufügen')

# Ruft Internetseite auf
if __name__ == "__main__":
    app.run(debug=True, port=5007)