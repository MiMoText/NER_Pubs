# NER_2021 enthält das Skript NER_0807.py

Input: Ordner data_in

Output: data_out

Es werden Funktionen für die eigentliche NER als auch für preprocessing
und Titelsuche zur Verfügung gestellt.
Alle Funktionsaufrufe befinden sich in Z.119-122
Bei Bedarf sind die Funktionen einzeln aufrufbar
Welche Dateiformate erwartet werden steht in den Kommentaren der Funktionen

Zur Suche nach Personen und Orten wurde spacy verwendet.

Zur Suche nach Werken ist spacy nicht geeignet, weil es sich dabei nicht um eine vortrainierte Kategorie handelt und zu wenig Daten für eigenes Training verfügbar waren.


Werktitel_short enthält 9412 Titel der Bibliographie.
Short: Die Titel wurden gekürzt indem Titelzusätze nach dem ersten Komma abgetrennt wurden,
Beispiel: "Haupttitel, Erzählung über x" wird zu "Haupttitel"

Werktitel_short_short enthält nur jeweils die zwei ersten Token eines Titels.
Das erhöht die Anzahl relevanter Treffer, kann aber auch zu falsch positiven Ergebnissen führen. 
