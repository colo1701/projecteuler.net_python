letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, 
           "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, 
           "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, 
           "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, 
           "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, 
           "Z": 26, }

def word_sum(word):
    result = 0
    for i in list(word): result += letters[i]
    return result

with open('pe_042_words.txt', 'r') as f:
    wordlist = [word.strip('"') for word in f.read().split(',')]

max_len = 0

for i in wordlist:
    if len(i) > max_len: max_len = len(i)

iterator = 2
triangles = [1]

while True:
    if max(triangles) > max_len * 26: break
    triangles.append(int(0.5 * iterator * (iterator+1)))
    iterator += 1

final_count = 0

for i in wordlist:
    if word_sum(i) in triangles: final_count += 1
        
print(final_count)