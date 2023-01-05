import math

def is_div(n, d):
    if n%d == 0: return True
    return False

def count_divs(n):
    count = 0
    for i in range(1, math.floor(math.sqrt(n))+1):
        if is_div(n, i): count += 2
    return count

def triangle(n):
    return n*(n+1)/2

iterator = 1

while count_divs(triangle(iterator)) <= 500:
    iterator += 1
print(int(triangle(iterator)))
