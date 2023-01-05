def is_good(n: int) -> bool:
    '''
    try if a given number equals the sum of its digits powered by 5
    '''
    
    n_str = str(n)
    checksum = 0
    for i in n_str: checksum += int(i)**5
    return checksum == n

# Für n-stellige Zahlen ist die größte Potenzsumme n*9^5.
# Für n = 7 ist das Minimum bereits 10^6.
# Das Maximum für n=7 liegt allerdings bei 7*9^5 = 413343.
# Also ist die obere Schranke 6-stellig.
# Die größte Potenzsumme im Fall n = 6 ist 6*9^5 = 354294.
# Damit ist das die obere Schranke.

accept = 0

for j in range(10, 354295):
    if is_good(j): accept += j

print(accept)
