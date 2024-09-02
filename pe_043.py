from itertools import permutations

perms_list = []
final_sum = 0

for i in permutations('1234567890', 10):
    perms_list.append(''.join(i))

denoms = [1, 2, 3, 5, 7, 11, 13, 17]

for j in perms_list:
    if all([int(j[k:k+3]) % denoms[k] == 0 for k in range(1, 8)]):
        final_sum += int(j)

print(final_sum)
