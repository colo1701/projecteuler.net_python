triplets = {}

def add_to_dict(i: int):
    if i in triplets.keys(): triplets[i] += 1
    else: triplets[i] = 1

for p in range(3, 1001):
    for c in range(3, int(p/2)+(p%2)):
        for b in range(1, c):
            a = p-c-b
            if a**2 + b**2 == c**2: add_to_dict(p)
              
print([k for k, v in triplets.items() if v == max(triplets.values())])
