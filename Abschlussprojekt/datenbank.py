
def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt

def abspeichern(art, anzahl, deadline):
    current_content = auslesen()
    new_content = current_content + f"\n{art}, {anzahl}, {deadline}"
    with open("database.csv", "w") as open_file:
        open_file.write(new_content)

def packliste_laden():
    packliste = auslesen()
    packliste_liste = packliste.split("\n")
    neue_liste = []
    for eintrag in packliste_liste:
        art, anzahl, deadline = eintrag.split(",")
        neue_liste.append([art, anzahl, deadline])
    return neue_liste