res_list = []
max = 100

for i in range(2, max+1):
    for j in range(2, max+1):
        res_list.append(i**j)

print(len(list(set(res_list))))