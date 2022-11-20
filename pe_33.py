from fractions import Fraction

def is_curious(z, n):
    z_str, n_str = str(z), str(n)
    
    conds = [n_str[1] == 0 and z_str[1] == 0]
    if any(conds): return False
    
    if z_str[0] == n_str[1] and int(z_str[1])/int(n_str[0]) == z/n: return True
    if z_str[1] == n_str[0] and int(n_str[1]) != 0 and int(z_str[0])/int(n_str[1]) == z/n: return True
    
    return False

zähler = 1
nenner = 1

for i in range(10, 100):
    for j in range(i+1, 100):
        if is_curious(i, j):
            zähler *= i
            nenner *= j

print(Fraction(zähler, nenner))