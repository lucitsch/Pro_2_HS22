# Read Me - Projekt "Ferienpackliste"

>## Inhalt
>* #### Ausgangslage des Projekts
>* #### Ziel des Programms
>## Benutzung
>* #### Installation
>* #### Ausführung
>* #### Detaillierte Ausführung
>* #### Vorhandene Funktionen
>## Ungelöste / unbearbeitete Probleme
>* #### Was wurde nicht gelöst?
>* #### Verbesserungen

## Inhalt
#### Ausgangslage des Projekts
Ich bin ein leidenschaftlicher Reiser. Wann immer die Möglichkeit besteht, packe ich meinen Koffer
und reise in der Welt umher. Oft reise ich an Ortschaften, welche bei einer speziellen Jahreszeit besonders schön sind.
Als Beispiel, letztes Jahr war ich in Puntacana in der Dominikanischen Republik. Ich war im Frühling dort,
da zu dieser Jahreszeit das Meerwasser am klarsten ist. Als ich für diese Ferien meine Kleider zusammenpacke wollte,
stellte ich, wenn es ums packen geht stelle ich mir immer dieselben Fragen:

Was soll ich alles mitnehmen?
Habe ich zu viel dabei?
Habe ich zu wenig dabei?
Habe ich etwas vergessen?

Um bei den nächsten Ferien diese Fragen einfacher beantworten zu können, habe ich mich entschieden 
ein Programm zu schreiben, welches das Packen für die Ferien einfacher machen sollte in dem es Vorschläge 
von Utensilien gibt, welche man mitnehmen könnten.

#### Ziel des Programms
Das Ziel dieses Programm sollte sein, dass dem Benutzer durch wenige Klicks eine Packliste zusammengestellt wird
nach seinen Bedürfnissen. Der User muss nur wenige Angaben machen, ob es zum Beispiel Sommer- oder Winterferien sind, 
oder ob es Sportferien oder erholsame Ferien sind. Das Programm schlägt dann unterschiedliche Utensilien vor, 
welche zu der entsprechenden Ferienart gut passen würden. So soll eine übersichtliche Packliste entstehen. 
Der User hat die Möglichkeit, individuelle Packlisten für sich zu erstellt.
<br>
<br>


## Benutzung
#### Installation
Um das Programm auszuführen zu können, müssen keine zusätzliche Pakete installiert werden.

#### Ausführung
Damit das Programm gestartet wird, muss die "main.py" Datei ausgeführt werden.
Um das Programm auszuführen muss sonst nichts spezielles beachtet werden, da es so einfach wie möglich gestalten wurde.
Auch ist kein Login nötig, da jeder individuell auf das Programm zugreifen kann. Die erstellten Packlisten des 
Users werden in einer Datenbank gespeichert, damit er die Möglichkeit hat zu einem späteren
Zeitpunkt seine erstellten Packlisten für die unterschiedlichen Destinationen wieder einzusehen.

#### Detaillierte Ausführung
Folglich wird in Stichworten aufgezählt, wie ein detaillierter Ablauf beim Verwenden des Programms aussehen könnte.

- Programm starten
- Packliste benennen / Ferien Art auswählen / Anzahl Tage angeben
- Speichern
- Utensilien anklicken welche zur Packliste gehören sollten
- Speichern (Packliste wird in der Datenbank gespeichert)
- Unter "Packlisten" können nun die erstellten Packlisten eingesehen werden
- Beim betätigen des "Abruf-Buttons" kann die Packliste angeschaut werden

#### Vorhandenen Funktionen
Das Projekt kann von jedem benutzt werden, egal ob Mann oder Frau, für Erwachsene oder Kinder.

Nebst dem Erstellen von den Packlisten, können auch noch individuelle Utensilien zur Packliste hinzugefügt werden.
Zusätzlich können die Packlisten mittels einer Datenbank abgespeichert werden um später wieder darauf zugreiffen
zu können. Ebenfalls gibt es eine Übersicht, die grafisch darstellt, welche Utensilien am meisten gebraucht werden 
und für welche für Art von Ferien, am meisten eine Packliste zusammengestellt wurde.
<br>
<br>


## Ungelöste / unbearbeitete Probleme
#### Was wurde nicht gelöst?
Wie beim Kapitel "Vorhandene Funktionen" geschrieben wurde, war ein weiteres Ziel der Arbeit,
dass dem User die Möglichkeit geschaffen wird, eine Grafik einzusehen die ausgibt für welche Art von Ferien am meisten
Packlisten erstellt wurden. Dieses Ziel wurde im Verlaufe der Arbeit nicht mehr verfolgt, da es aus meiner Sicht 
diese Möglichkeit nicht von Relevanz ist, da es keinen Mehrwert für den User generiert.

Ebenfalls sollte noch eine Möglichkeit erstellt werden, bei dem der User eigene Utensilien zur Packliste hinzufügen
könnte. Dies wurde nicht gelöst, da es beim programmieren Probleme gab mit den "Listen" in der Datenbank und das
Know-how nicht ausreichte um dieses Problem zu lösen.

#### Verbesserungen
- Es könnten noch mehr unterschiedliche Ferien-Arten erstellt werden
- Das Datum, wann die Ferien stattfinden könnte noch als Zusatzinformation dienen
- Mit der Eingabe für die "Anzahl-Tage" könnte noch verrechnet werden, wie viele Artikel eingepackt werden müssen
- Bei einigen Dateien könnte optimiert werden, weiterer "def()" verwenden anstelle von Code kopieren.