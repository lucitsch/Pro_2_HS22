# um Datum und Uhrzeit zu verwenden
import datetime
# Flask wird importiert, um eine Flask-Anwendung zu erstellen
# render_template um HTML-Templates zu rendern (darstellen)
from flask import Flask, render_template
# request importiert um auf Anforderungen des Benutzers zugreifen zu können
from flask import request
# wird verwendet um Daten aus der Datenbank zu lesen, speichern und verwalten
from Abschlussprojekt.datenbank import auslesen, abspeichern, packliste_laden, alle_speichern
# die Liste Sache wird importiert
from Abschlussprojekt.sachen_liste import sachen
# redirect wird importiert um die Navigation innerhalb der Anwendung zu steuern (HTTP-Umleitung)
from flask import redirect

# Flask-Anwendung mit dem Namen "Packliste" wird erstellt (nicht nötig)
app = Flask("Packliste")


# Starseite
# GET - um Daten von einem Server abzurufen. POST - um Daten an einen Server zu senden
@app.route("/", methods=["GET", "POST"])
# define, Funktion wird definiert
def add_new_packliste():
    if request.method == "GET":
        # index.html wird geladen , seitentitel ist optional und wird verwendet um Daten im Template anzuzeigen
        return render_template("index.html", seitentitel="eingabe")

    if request.method == "POST":
        ort = request.form['ort']
        typ = request.form['typ']
        anzahl = request.form['anzahl']
        # Fragt aktuellen Zeitpunkt ab und speicher sie in der Variablen deadline.
        # .now() gibt aktuelle Uhrzeit zurück. Wird in string verwandelt da es in der datenbank gespeichert wird
        deadline = str(datetime.datetime.now())
        # f-string  ermöglicht Variablen direkt in eine Textzeichenfolge einzubettet ohne mit str() umwandeln zu müssen
        print(f"Request From Ort: {ort}")
        print(f"Request Form Typ: {typ}")
        print(f"Request Form Anzahl: {anzahl}")
        print(f"Request Form Deadline: {deadline}")
        # abspeicher in Datenbank
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
    # lädt Daten aus der Datenbank und speichert sie in packliste_laden()
    packliste = packliste_laden()
    if request.method == "POST":
        # getlist gibt Zugriff auf mehrere Eingaben mit dem selben Namen und speichert sie in a
        a = request.form.getlist("name")
        # verweist auf das letzte Element in der packliste
        # packliste_last = packliste[-1]
        # append fügt das Element a am Ende der Liste an
        packliste.append(a)
        # aktualisiert das letzte Element der Liste
        #packliste[-1] = packliste_last
        # Liste und Seitentitel werden im Template eingebettet
    return render_template("packliste.html", liste=packliste, seitentitel="start")


@app.route("/abrufen", methods=['GET', 'POST'])
def abrufen():
    if request.method == 'POST':
        # ruft data ab und wird in eintrag gespeichert
        eintrag = request.form['data']
        return render_template("abrufen.html", eintrag=eintrag)


# Sommerpackliste
@app.route("/sommerkleider", methods=['GET', 'POST'])
def sommer():
    if request.method == 'POST':
        letzter_eintrag = request.form['letzter_eintrag']
        # split teilt einen String in eine Liste durch das trennzeichen \n
        alle_eintraege = auslesen().split("\n")
        # löscht das letzte Element aus der Liste
        del alle_eintraege[-1]
        name = request.form
        print((list(name)))
        # name = name[:-1]
        # verbindet die Elemente im name Objekt und trennt sie durch ;
        # join konvertiert Objekte in einen String. der String wird checks zugeordnet
        checks = ";".join(name)
        # entfernt , und []
        letzter_eintrag = letzter_eintrag.rstrip(", []")
        letzter_eintrag = letzter_eintrag + "," + str(checks)
        # am Ende angefügt
        alle_eintraege.append(letzter_eintrag)
        alle_speichern(alle_eintraege)
        return redirect("/packlisten")

    letzter_eintrag = auslesen().split("\n")[-1]
    kategorien = ["Sommerbekleidung", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien, letzter_eintrag=letzter_eintrag)


# Winterpackliste
@app.route("/winterkleider", methods=['GET', 'POST'])
def winter():
    if request.method == 'POST':
        letzter_eintrag = request.form['letzter_eintrag']
        # split teilt einen String in eine Liste durch das trennzeichen \n
        alle_eintraege = auslesen().split("\n")
        # löscht das letzte Element aus der Liste
        del alle_eintraege[-1]
        name = request.form
        print((list(name)))
        # name = name[:-1]
        # verbindet die Elemente im name Objekt und trennt sie durch ;
        # join konvertiert Objekte in einen String. der String wird checks zugeordnet
        checks = ";".join(name)
        # entfernt , und []
        letzter_eintrag = letzter_eintrag.rstrip(", []")
        letzter_eintrag = letzter_eintrag + "," + str(checks)
        # am Ende angefügt
        alle_eintraege.append(letzter_eintrag)
        alle_speichern(alle_eintraege)
        return redirect("/packlisten")

    letzter_eintrag = auslesen().split("\n")[-1]
    kategorien = ["Winterkleider", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien, letzter_eintrag=letzter_eintrag)


# Skipackliste
@app.route("/skikleider", methods=['GET', 'POST'])
def ski():
    if request.method == 'POST':
        letzter_eintrag = request.form['letzter_eintrag']
        # split teilt einen String in eine Liste durch das trennzeichen \n
        alle_eintraege = auslesen().split("\n")
        # löscht das letzte Element aus der Liste
        del alle_eintraege[-1]
        name = request.form
        print((list(name)))
        # name = name[:-1]
        # verbindet die Elemente im name Objekt und trennt sie durch ;
        # join konvertiert Objekte in einen String. der String wird checks zugeordnet
        checks = ";".join(name)
        # entfernt , und []
        letzter_eintrag = letzter_eintrag.rstrip(", []")
        letzter_eintrag = letzter_eintrag + "," + str(checks)
        # am Ende angefügt
        alle_eintraege.append(letzter_eintrag)
        alle_speichern(alle_eintraege)
        return redirect("/packlisten")

    letzter_eintrag = auslesen().split("\n")[-1]
    kategorien = ["Skibekleidung", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien, letzter_eintrag=letzter_eintrag)


# Strandkleider
@app.route("/strandkleider", methods=['GET', 'POST'])
def strand():
    if request.method == 'POST':
        letzter_eintrag = request.form['letzter_eintrag']
        # split teilt einen String in eine Liste durch das trennzeichen \n
        alle_eintraege = auslesen().split("\n")
        # löscht das letzte Element aus der Liste
        del alle_eintraege[-1]
        name = request.form
        print((list(name)))
        # name = name[:-1]
        # verbindet die Elemente im name Objekt und trennt sie durch ;
        # join konvertiert Objekte in einen String. der String wird checks zugeordnet
        checks = ";".join(name)
        # entfernt , und []
        letzter_eintrag = letzter_eintrag.rstrip(", []")
        letzter_eintrag = letzter_eintrag + "," + str(checks)
        # am Ende angefügt
        alle_eintraege.append(letzter_eintrag)
        alle_speichern(alle_eintraege)
        return redirect("/packlisten")

    letzter_eintrag = auslesen().split("\n")[-1]
    kategorien = ["Strandbekleidung", "Reisedokumente", "Hygiene", "Finanzen", "Handy", "Unterhaltung"]
    return render_template('pack_auswahl.html', sachen=sachen, kategorien=kategorien, letzter_eintrag=letzter_eintrag)


@app.route("/hinzufügen", methods=['GET', 'POST'])
def add_sachen():
    if request.method == 'POST':
        # Hinzufügen von Utensilien der Packliste (Fehler da es unvollständig ist)
         sachen["Persönliche Artikel"].append(value)
    return render_template('Sachen_Hinzufügen.html')


# Ruft Internetseite auf
if __name__ == "__main__":
    app.run(debug=True, port=5007)