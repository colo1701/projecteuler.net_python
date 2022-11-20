def is_pyth(a, b, c):
    if a + b + c == 1000 and a**2 + b**2 == c**2: return True
    return False

for a in range(1, 334):
    for b in range(2, 501):
        for c in range(3, 998):
            if is_pyth(a, b, c): 
                print(a*b*c)
                break