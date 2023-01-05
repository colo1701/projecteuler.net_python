def shareable20(n):
    for i in range(1, 21):
        if n%i != 0: return False
    return True

iterator = 380

while True:
    if shareable20(iterator):
        print(iterator)
        break
    iterator += 380
