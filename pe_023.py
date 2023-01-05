import numpy as np
import time

def is_div(N, n):
    return (N/n)%1 == 0

def is_abu(N: int) -> bool:
    divs = []
    for i in range(1, int(np.ceil(N/2))+1):
        if is_div(N, i): divs.append(i)
    return sum(divs) > N

abus_list = []
for i in range(1, 28124):
    if is_abu(i): abus_list.append(i)

abus = np.array(abus_list)
print(abus)

################################################################################

def is_abu_sum(N: int) -> bool:
    for i in range(len(abus)):
        if abus[i] > N-12: return False
        elif N-abus[i] in abus: return True
    return False

non_abu_sum = 276 # Die Zahlen 1-23 sind per Definition ausgeschlossen

for i in range(24, 28124):
    if not is_abu_sum(i): 
        non_abu_sum += i

print(non_abu_sum)
