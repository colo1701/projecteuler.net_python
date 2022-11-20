import csv
import numpy as np

# Funktion, die einen Text in die Summe seiner Buchstabenwerte umwandelt
# Großbuchstaben werden mit 'ord(x)-64' umgewandelt, Kleinbuchstaben mit 'ord(x)-96'.
def text_to_numsum(word: str) -> int:
    num = []
    for x in word: num.append(ord(x)-64)
    return sum(num)

# Datei als Liste speichern und sortieren
with open("p022_names.txt") as source_file:
    name_list = list(csv.reader(source_file, delimiter = ","))[0]
    name_list.sort()

source_file.close()

num_names = len(name_list)
num_values = np.zeros(num_names, np.int64)

for i in range(num_names): num_values[i] = text_to_numsum(name_list[i])*(i+1)

print(sum(num_values))