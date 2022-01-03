import re
import spacy
import glob
import os

# ###### Extract titles ###############
# read xml-files, containing work titles
# work title are tagged with <ti></ti>


def title_extraction():
    # creating list of files to extract
    txt_paths = glob.glob("data_in/title_extraction/*.xml")  # Save the (relative) paths of all .txt files in a list
    print("{} text file(s) have been found. \n".format(len(txt_paths)))

    for path in txt_paths:
        file_name = os.path.splitext(os.path.basename(path))[0]
        with open("data_in/title_extraction/" + file_name + ".xml", encoding="utf-8") as file:
            gesamtertext = file.read()

        # find tags
        titel = re.findall("<ti>(.*)</ti>", gesamtertext)
        print(titel)

        # write titles to file
        # title file is written to "data in"-folder because it is just an intermediate step
        # TODO am besten sowohl in data in als auch in data out schreiben
        f = open("data_in/titles.csv", "a", encoding="utf8")
        for item in titel:
            f.writelines(str(item) + "\n")
        f.close()


# ####### Shorten titles #####################
# This function takes data_in/titles.csv as input
# Output are the same titles but in shortened form


def shorten_titles():
    # open input file
    with open("data_in/titles.csv", encoding="utf8") as file:
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

    f = open("data_in/titles_short.csv", "a", encoding="utf8")
    for item in list_titles_short2:
        f.writelines(str(item) + ",\n")
    f.close()


# ##################### Search for known titles in unknown files #####################


def titlesearch():
    with open("data_in/titles_short.csv", encoding="utf-8") as file:
        data = file.read()

    data = re.escape(data)
    rowlist = data.split(chr(10))

    txt_paths = glob.glob("data_in/titelsuche/*.txt")  # Save the (relative) paths of all .txt files in a list
    print("{} text file(s) have been found. \n".format(len(txt_paths)))

    for path in txt_paths:
        file_name = os.path.splitext(os.path.basename(path))[0]  # Path-string stripped of "data_in/titelsuche" and .extension

        with open("data_in/titelsuche/" + file_name + ".txt", encoding="utf-8") as file:
            my_text = file.read()

        my_text = re.escape(my_text)

    # Zeilenliste2 enthält alle Titel der Bibliographie
    # zeilenliste2 wird gesäubert

        zeilenliste2 = []
        for item in rowlist:
            item_escaped = re.escape(item)
            item_cleaned = re.sub(",", "", item_escaped)
            zeilenliste2.append(item_cleaned)

        #print(zeilenliste2)


        ergebnisliste = []
        #ergebnis = re.findall(zeilenliste2[0], my_text)
        # print(ergebnis)

        for i in range(len(rowlist)):
            ergebnis = re.findall(zeilenliste2[i], my_text)
            if ergebnis:
                ergebnisliste.append(ergebnis)
       # print(ergebnisliste)
        with open("data_out/titelsuche/" + file_name +"_titel" ".txt","w", encoding="utf-8") as file:
            for item in ergebnisliste:
                file.write("%s\n" % item_cleaned)



# ############ NE-Suche ######################
def ner():

    nlp_de = spacy.load("de_core_news_md")

    txt_paths = glob.glob("data_in/ner/*.txt")  # Save the (relative) paths of all .txt files in a list
    print("{} text file(s) have been found. \n".format(len(txt_paths)))

    for path in txt_paths:
        file_name = os.path.splitext(os.path.basename(path))[0]  # Path-string stripped of "data_in/titelsuche" and .extension

        with open("data_in/ner/" + file_name + ".txt", encoding="utf-8") as file:
            data = file.read()

        doc = nlp_de(data)

        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)


        with open("data_out/ner/"+file_name+"_ner.txt", "w", encoding="utf-8") as file:
            file.write("start \n")
            for ent in doc.ents:
                file.write(str(ent.text) + ", " + str(ent.start_char) + ", " + str(ent.end_char) + ", " + str(ent.label_) + "\n")


# ############ Funktionsaufrufe #########################

title_extraction()
# titel_kuerzen()
#titelsuche()
#ner()
