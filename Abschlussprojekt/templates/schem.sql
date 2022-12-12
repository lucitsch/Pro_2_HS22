-- Tabellen namen posts werden gelöscht damit sie nicht durcheinander kommen

DROP TABLE IF EXISTS posts;

-- hiermit wird eine Tabelle erstellt id = Primärschlüssel / created = Zeit / NOT NULL = darf nicht leer sein / Deafult = Current_Timestamp
-- title = Titel des Beitrags / content = Der Inhalt des Beitrags

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
