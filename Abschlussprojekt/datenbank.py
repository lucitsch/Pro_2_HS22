
def auslesen():
    # Liest den Inhalt der Datenbank und weist ihn der Variablen Inhalt zu
    # r ist der "read"-Modus. Inhalt der Datei wird eingelesen
    with open("database.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def abspeichern(ort, typ, anzahl, deadline):
    current_content = auslesen()
    # neue Zeichenfolge wird erstellt und Inhalt wird um eine neue Zeile erweitert
    new_content = current_content + f"\n{ort}, {typ}, {anzahl}, {deadline}, []"
    # w ist der write-Modus, so wird der alte Inhalt ersetzt
    with open("database.csv", "w") as open_file:
        open_file.write(new_content)


# Liste von data_liste wird als Parameter entgegen genommen
def alle_speichern(data_liste):
    # database.csv wird im write Modus geöffnet jeder Eintrag in data_liste wird als neue Zeile geschrieben
    with open("database.csv", "w") as open_file:
        for item in data_liste:
            open_file.write(item + "\n")


def packliste_laden():
    # Inhalt der database.csv wird gelesen und in packliste gespeichert
    packliste = auslesen()
    # Inhalt wird gesplitet und neue Zeile wird als Trennzeichen verwendet
    packliste_liste = packliste.split("\n")
    # neue Leere Liste wird erstellt
    neue_liste = []
    # Eintraege werden mit Komma getrennt und in neue_liste hinzugefuegt
    for eintrag in packliste_liste:
        if len(eintrag) != 0:
            ort, typ, anzahl, deadline, aufzaehlung = eintrag.split(",")
            neue_liste.append([ort, typ, anzahl, deadline])
    return neue_liste
