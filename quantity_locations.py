import re
from collections import Counter

with open("./results_and_evaluation/annotated_by_hand/rieger_orte.txt", encoding="utf8") as my_file:
    my_text = my_file.read()

orte = re.findall("\%.+?\s", my_text)
print(orte)

orte_sortiert = Counter(orte).most_common()
print(orte_sortiert)

with open("data_out/rieger_häufigkeit_orte_output.txt_häufigkeit_orte_output.txt", "w", encoding="utf8") as output_file:
    for item in orte_sortiert:
        output_file.write(str(item) + ",\n")