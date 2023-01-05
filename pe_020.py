import math

def fact_dig_sum(N: int) -> int:
    summe = 0
    for i in str(math.factorial(N)): summe += int(i)
    return summe

fact_dig_sum(100)
