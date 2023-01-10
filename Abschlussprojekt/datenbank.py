def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def abspeichern(ort, typ, anzahl, deadline):
    current_content = auslesen()
    new_content = current_content + f"\n{ort}, {typ}, {anzahl}, {deadline}, []"
    with open("database.csv", "w") as open_file:
        open_file.write(new_content)


def alle_speichern(data_liste):

    with open("database.csv", "w") as open_file:
        for item in data_liste:
            open_file.write(item + "\n")


def packliste_laden():
    packliste = auslesen()
    packliste_liste = packliste.split("\n")
    neue_liste = []
    for eintrag in packliste_liste:
        if len(eintrag) != 0:
            ort, typ, anzahl, deadline, aufzaehlung = eintrag.split(",")
            neue_liste.append([ort, typ, anzahl, deadline])
    return neue_liste


