products = []

def is_pan(string: str) -> bool:
    for i in range(len(string)):
        if string.count(string[i]) > 1: return False
    return True

for a in range(2, 291):
    for b in range(1, int(78885/a)+2):
        term = str(a) + str(b) + str(a*b)
        if is_pan(term) and len(term) == 9 and term.count("0") == 0 and not a*b in products: products.append(a*b)    
                
print(sum(products))
