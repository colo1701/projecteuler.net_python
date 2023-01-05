def collatz_follow(n):
    if n%2 == 0: return n/2
    return (3*n)+1

def len_collatz(n):
    count = 1
    coll_in = n
    while True:
        if coll_in == 1:
            return count
            break
        coll_in = collatz_follow(coll_in)
        count += 1

results = [0, 0]

for i in range(1000000):
    if len_collatz(i+1) > results[1]:
        results[0] = i+1
        results[1] = len_collatz(i+1)

print(results[0])
