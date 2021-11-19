import re
import csv
import spacy
import glob
import sys

# ###### Extrahiere Titel ###############
# Hier werden getaggte XML-Dateien eingelesen
# Es werden alle Elemente extrahiert, die mit <ti></ti> getaggt sind


def title_extraction():
    # Liste der Dateien
    dateiliste = glob.glob("data_in/*.xml")

    # Jedes Element der Liste durchsuchen
    for datei in dateiliste:
        try:
            d = open(datei, encoding="utf8")
        except:
            print("Dateizugriff nicht erfolgreich")

        # Text einlesen
        gesamtertext = d.read()

        # Zugriff beenden
        d.close()

        # Suchtext suchen
        titel = re.findall("<ti>(.*)</ti>", gesamtertext)
        print(titel)

        # alle gefundenen Titel in Datei schreiben
        # kommt in data_in, weil ich da nochmal drauf zugreife
        f = open("data_in/Werktitel.csv", "a", encoding="utf8")
        for item in titel:
            f.writelines(str(item) + "\n")


# ####### Werktitel kürzen #####################
def titel_kuerzen():
    with open("data_in/Werktitel.csv", encoding="utf8") as file:
        data = file.readlines()

    list_titles_short = []

    for item in data:
        title_short = re.sub("(,.*)\\n", "", item)
        list_titles_short.append(title_short)

    print(list_titles_short)

    list_titles_short2 = []
    for item in list_titles_short:
        title_short2 = re.sub("\n", "", item)
        list_titles_short2.append(title_short2)

    print(list_titles_short2)

    f = open("data_in/Werktitel_short.csv", "a", encoding="utf8")
    for item in list_titles_short2:
        f.writelines(str(item) + ",\n")

# ##################### Titelsuche #####################
def titelsuche():
    with open("data_in/Werktitel_short.csv", encoding="utf-8") as file:
        data = file.read()
    data = re.escape(data)
    zeilenliste = data.split(chr(10))
    # print(zeilenliste)

    with open("data_in/Grimm_Hartwig_Moralistik_Die_französische_Revolution_241-243.txt", encoding="utf-8") as file:
        my_text = file.read()

    my_text = re.escape(my_text)

# Zeilenliste2 enthält alle Titel der Bibliographie
# zeilenliste2 wird gesäubert
    zeilenliste2 = []
    for item in zeilenliste:
        item_escaped = re.escape(item)
        item_cleaned = re.sub(",", "", item_escaped)
        zeilenliste2.append(item_cleaned)

    print(len(zeilenliste2))

    #ergebnis = re.findall(zeilenliste2[0], my_text)
    #print(ergebnis)
    ergebnisliste = []
    for i in range(len(zeilenliste)):
        ergebnis = re.findall(zeilenliste2[i], my_text)
        if ergebnis:
            ergebnisliste.append(ergebnis)
    print(ergebnisliste)
    with open("data_out/Grimm_Hartwig_Moralistik_Die_französische_Revolution_241-243_titel.txt", "a", encoding="utf-8") as file:
        for item in ergebnisliste:
            file.write("%s\n" % item)



# ############ NE-Suche ######################
def ner():

    nlp_de = spacy.load("de_core_news_md")

    with open("data_in/rieger.txt", encoding="utf-8") as file:
        data = file.read()

    doc = nlp_de(data)

    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


    with open("data_out/rieger_ner.txt", "w", encoding="utf-8") as file:
        file.write("start \n")
        for ent in doc.ents:
            file.write(str(ent.text) + ", " + str(ent.start_char) + ", " + str(ent.end_char) + ", " + str(ent.label_) + "\n")


# ############ Funktionsaufrufe #########################

# title_extraction()
# titel_kuerzen()
# titelsuche()
ner()
