from num2words import num2words

def count_letters(string):
    number = 0
    for i in string:
        if i != " " and i != "-": number += 1
    return number

def string_gen(n):
    string = ""
    for i in range(n): string += num2words(i+1)
    return string
    
count_letters(string_gen(1000))
