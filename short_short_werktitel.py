import re

with open("data_in/Werktitel_short_0406.csv", encoding="utf-8") as file:
    data = file.read()


titel = re.findall("(.+?\s.+?\s).+?,\n?", data)

print(titel)
print(len(titel))



with open("data_out/Werktitel_short_short.csv", "w", encoding="utf-8") as file:
    for i in range(len(titel)):
        file.write(str(titel[i]) + "\n")






