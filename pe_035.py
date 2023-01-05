import numpy as np

def is_prime(n: int) -> bool:
    '''
    check whether a given number is a prime number or not
    '''
    if n%2 == 0: return False
    for i in range(3, int(np.sqrt(n))+1, 2):
        if n%i == 0: return False
    return True

def rotate(n: int) -> int:
    '''
    rotate the digits of a given number to the left
    first digit will become the last digit of the new number
    '''
    num_in = list(str(n))
    num_out = []
    for i in num_in[1:]: num_out.append(i)
    num_out.append(num_in[0])
    rotator = "".join(j for j in num_out)
    return int(rotator)

def rot_collection(n: int) -> list:
    '''
    collect all possible rotations of a given number in a list
    '''
    rots_out = [n]
    for _ in range(len(str(n))-1):
        n = rotate(n)
        rots_out.append(n)
    return rots_out

def is_circ_prime(n: int) -> bool:
    '''
    check whether all rotations of a given number are prime numbers or not
    '''
    if "0" in str(n): return False
    tries = [is_prime(i) for i in rot_collection(n)]
    return all(tries)

counter = 1

for a in range(3, 1000000, 2):
    if is_circ_prime(a): counter += 1
        
print(counter)
