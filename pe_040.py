irrational = ""

runner = 1
while len(irrational) < 1000000:
    irrational += str(runner)
    runner += 1

prod = 1

for i in range(0, 7): prod *= int(irrational[(10**i)-1])

print(prod)
