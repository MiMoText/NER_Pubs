# Named Entity Recognition for Scholary Publications

Input: data_in
Output: data_out

Usage: Execution via main.py
contains the following functions:
- title_extraction
- shorten_titles
- titlesearch
- rdf_query

every function can be used independently
if u execute main.py without changes it will use standard values and corpus from data_in

Directories:
# Subdirectories TODO
# (vorher ausmisten)
- data_in
- data_out
- results_and_evaluation

This package provides functionality for extracting Named Entities, work titles.
Including all relevant preprocessing steps and quality evaluation after the search.
For regular named entities spacy was used. For extracting work titles a method specified for 
the MimoText corpus is provided.



Werktitel_short enthält 9412 Titel der Bibliographie.
Short: Die Titel wurden gekürzt indem Titelzusätze nach dem ersten Komma abgetrennt wurden,
Beispiel: "Haupttitel, Erzählung über x" wird zu "Haupttitel"

Werktitel_short_short enthält nur jeweils die zwei ersten Token eines Titels.
Das erhöht die Anzahl relevanter Treffer, kann aber auch zu falsch positiven Ergebnissen führen. 
