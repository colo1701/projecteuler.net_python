import numpy as np
import math

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, math.floor(np.sqrt(n))+1):
        if n%i == 0: return False
    return True

def list_up(N):
    primes = [2]
    testnum = 3
    while len(primes) < N:
        if is_prime(testnum): primes.append(testnum)
        testnum += 2
    return primes[-1]

list_up(10001)