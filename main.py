import spacy
import glob
import os
import rdflib
import re
from collections import Counter
from pathlib import Path


# ######### Query rdf graph ###################
# The bibliographic data is available as an rdf graph.
# This funktion extracts author names and work titles from the graph

def rdf_query():

    # Lade den Bibliographie-Graphen
    g = rdflib.Graph()
    g.load("data_in/rdf/bibliographie.rdf")

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


# ###### Extract titles ###############
# read xml-files, containing work titles
# work title are tagged with <ti></ti>

def title_extraction():
    # creating list of files to extract titles from
    txt_paths = glob.glob("data_in/title_extraction/*.xml")
    print("{} text file(s) have been found. \n".format(len(txt_paths)))

    for path in txt_paths:
        file_name = os.path.splitext(os.path.basename(path))[0]
        with open("data_in/title_extraction/" + file_name + ".xml", encoding="utf-8") as file:
            gesamtertext = file.read()

        # find title tags
        titel = re.findall("<ti>(.*)</ti>", gesamtertext)
        print(titel)

        # write titles to file
        # title file is written to "data in"-folder because this is just an intermediate step
        # TODO am besten sowohl in data in als auch in data out schreiben
        f = open("data_in/other_files/titles.csv", "a", encoding="utf8")
        for item in titel:
            f.writelines(str(item) + "\n")
        f.close()


# ####### Shorten titles #####################
# This function takes data_in/titles.csv as input
# Output are the same titles but in shortened form


def shorten_titles():
    # open input file
    with open("data_in/other_files/titles.csv", encoding="utf8") as file:
        data = file.readlines()

    # create list of shortened titles and print them to console
    list_titles_short = []
    for item in data:
        title_short = re.sub("(,.*)\\n", "", item)
        list_titles_short.append(title_short)

    print(list_titles_short)

    # create shorter version of titles
    list_titles_short2 = []
    for item in list_titles_short:
        title_short2 = re.sub("\n", "", item)
        list_titles_short2.append(title_short2)

    print(list_titles_short2)
    path_titles_short = "data_in/other_files/titles_short.csv"
    f = open("data_in/other_files/titles_short.csv", "a", encoding="utf8")
    for item in list_titles_short2:
        f.writelines(str(item) + ",\n")
    f.close()




# ##################### Search for known titles in unknown files #####################

def titlesearch():
    with open("data_in/other_files/titles_short.csv", encoding="utf-8") as file:
        data = file.read()

    data = re.escape(data)
    rowlist = data.split(chr(10))

    txt_paths = glob.glob("data_in/titlesearch/*.txt")
    print("{} text file(s) have been found. \n".format(len(txt_paths)))

    for path in txt_paths:
        file_name = os.path.splitext(os.path.basename(path))[0]

        with open("data_in/titlesearch/" + file_name + ".txt", encoding="utf-8") as file:
            my_text = file.read()

        my_text = re.escape(my_text)
    # list of rows 2 contains all title appearing in bibliographic
    # this list will be cleaned from characters which aren't letters or numbers

        zeilenliste2 = []
        for item in rowlist:
            item_escaped = re.escape(item)
            item_cleaned = re.sub(",", "", item_escaped)
            zeilenliste2.append(item_cleaned)

        ergebnisliste = []
        for i in range(len(rowlist)):
            ergebnis = re.findall(zeilenliste2[i], my_text)
            if ergebnis:
                ergebnisliste.append(ergebnis)

        with open("data_out/titlesearch/" + file_name +"_titel" ".txt","w", encoding="utf-8") as file:
            for item in ergebnisliste:
                file.write("%s\n" % item_cleaned)


# ############ Finding Named Entities ######################

def ner():
    nlp_de = spacy.load("de_core_news_md")
    txt_paths = glob.glob("data_in/ner/*.txt")
    print("{} text file(s) have been found. \n".format(len(txt_paths)))

    for path in txt_paths:
        file_name = os.path.splitext(os.path.basename(path))[0]
        with open("data_in/ner/" + file_name + ".txt", encoding="utf-8") as file:
            data = file.read()

        doc = nlp_de(data)
        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)

        with open("data_out/ner/"+file_name+"_ner.txt", "w", encoding="utf-8") as file:
            file.write("start \n")
            for ent in doc.ents:
                file.write(str(ent.text) + ", " + str(ent.start_char) + ", " + str(ent.end_char) + ", " + str(ent.label_) + "\n")


def quantity_locations():
    with open("./results_and_evaluation/annotated_by_hand/rieger_orte.txt", encoding="utf8") as my_file:
        my_text = my_file.read()

    orte = re.findall("\%.+?\s", my_text)
    print(orte)

    orte_sortiert = Counter(orte).most_common()
    print(orte_sortiert)

    with open("data_out/rieger_häufigkeit_orte_output.txt_häufigkeit_orte_output.txt", "w",
              encoding="utf8") as output_file:
        for item in orte_sortiert:
            output_file.write(str(item) + ",\n")

# ############ Calling the functions #########################

# To call functions just delete #
# If you don't pass any function parameters default data from MimoText will be used.
# TODO parameter für jede Funktion aufschreiben
# todo aufschreiben was für Default MimoText-Daten das sind


title_extraction()
# shorten_titles()
# titlesearch()
# ner()
# rdf_query()
