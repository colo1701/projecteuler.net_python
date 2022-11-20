import numpy as np
import math

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, math.floor(np.sqrt(n))+1):
        if n%i == 0: return False
    return True

def sum_up(N):
    primesum = 0
    for i in range(N):
        if is_prime(i): primesum += i
    return primesum

sum_up(2000000)