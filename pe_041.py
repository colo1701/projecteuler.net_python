'''
To reduce the amount of potential pandigital numbers one can have a look on common rules for dividability.
E.g. even numbers (n%2 = 0) can't be prime numbers (except 2).
But one can alo set a limit for the highest possible pandigital prime number by checking the diviability by 3. 
A number n is dividable by 3 if the sum of its digits is dividable by 3. 
If we have look on 9-digit pandigital numbers,we can say that the sum of their digits is always 45 (1+2+3+4+5+6+7+8+9), 
which can be divided by 3, so these numbers can't be prime numbers.
The same thing can be observed for 8-digit numbers. Their digit sum is always 36 (1+2+3+4+5+6+7+8), 
which can also be divided by 3. This fact alone limits the highest possible pandigital prime number to be lower or equal to 7654321.
Luckily modern computers don't have any problems doing such calculations on 7-digit numbers so this helps us a lot, 
finding the right solution to this challenge.
'''

import math
from time import time

def is_prime(n):
    if n == 2: return True
    if n == 1 or n % 2 == 0: return False
    tested = [2, 3]
    for i in range(5, int(math.sqrt(n))+1, 2):
        is_prime = True
        for j in tested:
            if i % j == 0:
                is_prime = False
                break
        if is_prime: tested.append(i)
    return all(n % i != 0 for i in tested)

check_value = 7654323
t0 = time()
counter = 0

while True:   
    check_value -= 2

    n_list = list(str(check_value))
    n_list_sorted = n_list.copy()
    n_list_sorted.sort()
    
    if n_list_sorted == ['1', '2', '3', '4', '5', '6', '7'] and n_list[-1] != '5':
        counter += 1
        testbool = is_prime(check_value)
        print(f"{check_value}: {testbool}")
        if testbool: 
            print(f"Done in {round(time()-t0, 2)} seconds!")
            break
        if counter%100 == 0:
            print(f"{counter} numbers checked after {round(time()-t0, 2)} seconds!")