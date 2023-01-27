nums = []

def is_pan(abc: str) -> bool:
    for i in range(1, 10):
        if not str(i) in abc: return False
    return True

for i in range(1, 50000):
    word = ""
    
    multi = 1
    while len(word) < 9:
        word += str(i * multi)
        multi += 1
    
    if len(word) == 9:
        if is_pan(word): nums.append(word)

nums.sort()

print(nums[-1])
