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
- data_in
- data_out
- results_and_evaluation

This package provides functionality for extracting Named Entities, work titles.
Including all relevant preprocessing steps and quality evaluation after the search.
For regular named entities spacy was used. For extracting work titles a method specified for 
the MimoText corpus is provided.


