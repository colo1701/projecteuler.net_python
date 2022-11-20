def div_sum(N: int) -> int:
    summe = 0
    for i in range(1,int(N/2)+1):
        if N%i == 0: summe += i
    return summe

summe2 = 0

for j in range(10001):
    if j == div_sum(div_sum(j)) and j != div_sum(j): 
        summe2 += j
print(summe2)