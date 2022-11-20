import numpy as np

def dec_to_bin(n: int) -> int:
    lim = int(np.log2(n))+1
    bin_array = np.zeros(lim, np.uint8)
    bin_array[0] = 1
    rest = n - 2**(lim-1)
    for j in range(lim-2, -1, -1):
        if rest >= 2**j:
            bin_array[lim - 1 - j] = 1
            rest -= 2**j
    return bin_array

def is_palin(n: int) -> bool:
    return str(n) == str(n)[::-1]

palin_sum = 0

for a in range(1, 1000000, 2):
    bin_a = "".join(str(b) for b in dec_to_bin(a))
    if is_palin(a) and is_palin(bin_a): palin_sum += a

print(palin_sum)