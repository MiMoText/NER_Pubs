# Named Entity Recognition for Scholary Publications

Input: data_in
Output: data_out

Usage: Execution via main.py
contains functions:
- (...)
every function can be used independently
if u execute main.py without changes it will use standard values and corpus from data_in

Directory data in
Subdirectories (in alphabetical order):
- other_files
- rdf
- titelsuche #Achtung, das soll raus
- txt_files
- xml_files


Es werden Funktionen für die eigentliche NER als auch für preprocessing
und Titelsuche zur Verfügung gestellt.
Alle Funktionsaufrufe befinden sich in Z.142-145
Bei Bedarf sind die Funktionen einzeln aufrufbar
Welche Dateiformate erwartet werden steht in den Kommentaren der Funktionen

Zur Suche nach Personen und Orten wurde spacy verwendet.

Zur Suche nach Werken ist spacy nicht geeignet, weil es sich dabei nicht um eine vortrainierte Kategorie handelt und zu wenig Daten für eigenes Training verfügbar waren.


Werktitel_short enthält 9412 Titel der Bibliographie.
Short: Die Titel wurden gekürzt indem Titelzusätze nach dem ersten Komma abgetrennt wurden,
Beispiel: "Haupttitel, Erzählung über x" wird zu "Haupttitel"

Werktitel_short_short enthält nur jeweils die zwei ersten Token eines Titels.
Das erhöht die Anzahl relevanter Treffer, kann aber auch zu falsch positiven Ergebnissen führen. 
