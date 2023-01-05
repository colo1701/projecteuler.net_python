import math

palins = []

def is_palin(n):
    for i in range(math.floor(len(str(n))/2)):
        if str(n)[i] != str(n)[-i-1]: return False
    return True

for i in range(1000):
    for j in range(1000):
        if is_palin(i*j): palins.append(i*j)

print(max(palins))
