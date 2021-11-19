import numpy as np
import rdflib
import re
from collections import defaultdict
import csv
import os

# Lade den Bibliographie-Graphen
g = rdflib.Graph()
g.load("data_in\\bibliographie.rdf")

query = ("""
 PREFIX loc: <http://www.w3.org/2007/uwa/context/location.owl#>
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX co: <http://purl.org/ontology/co/core#>
    PREFIX biro: <http://purl.org/spar/biro/>
    PREFIX frbr: <http://purl.org/vocab/frbr/core#>
    PREFIX prism: <http://prismstandard.org/namespaces/basic/2.0/>
    SELECT DISTINCT ?au ?ti 
                        WHERE {
                           ?expression dcterms:creator ?au . 
                           ?expression j.0:title ?ti .                          
                            
                            
                         
                            } LIMIT 100""")

results = g.query(query)

print("====== RDF Query ======")
print("The query returned " + str(len(results)) + " results")

with open("data_out\\author_title.csv", "w", encoding="utf-8") as csvfile:
    for row in results:
        csvfile.write("%s is creator of %s" % row + "\n")



for row in results:
    print("%s is creator of %s" % row)
g.close()

