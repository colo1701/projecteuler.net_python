import numpy as np
from time import time

def is_prime(n: int) -> bool:
    if n == 2: return True
    if n <= 1 or n%2 == 0: return False
    for i in range(3, int(np.sqrt(n))+1, 2):
        if n%i == 0: return False
    return True

def remove_r(n: int) -> int:
    return int(str(n)[:-1])

def remove_l(n: int) -> int:
    return int(str(n)[1:])

final_count = 0
final_sum = 0
a = 11


while True:
    a_values = [a]
    
    a = a_values[0]
    for _ in range(len(str(a))-1):
        a = remove_l(a)
        a_values.append(a)
    
    a = a_values [0]
    for _ in range(len(str(a))-1):
        a = remove_r(a)
        a_values.append(a)
    
    if all([is_prime(c) for c in a_values]):
        final_count += 1
        final_sum += a_values[0]
    
    add_num = 2
    
    while True:
        try_sum = str(a_values[0] + add_num)
        if any(int(d)%2 == 0 for d in try_sum) and len(try_sum) > 2: add_num += 2
        else: break
    
    a = a_values[0] + add_num
    
    if final_count == 11: 
        print(final_sum)
        break
