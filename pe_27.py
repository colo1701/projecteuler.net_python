import numpy as np

def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(np.sqrt(n))+1):
        if n%i == 0: return False
    return True

def cons_count(x, y):
    n = 0
    while is_prime((n**2)+(x*n)+y): n += 1
    return n

a_max = 0
b_max = 0
cons_max = 0

a = range(-999,1000)
b = range(-1000,1001)

for i in a:
    for j in b:
        if cons_count(i, j) > cons_max: a_max, b_max, cons_max = i, j, cons_count(i, j)

print(a_max*b_max)