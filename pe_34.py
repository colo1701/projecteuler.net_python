from math import factorial as fact

# Bei 8 Stellen ist das Minimum 10^7 aber das Maximum ~2.9*10^6.
# Daher kann die höchste Zahl 7-stellig sein.
# Eine obere Schranke ist also 7*9! = 2540160

def fact_sum(n: int) -> bool:
    check_sum = 0
    n_str = str(n)
    for i in n_str: check_sum += fact(int(i))
    return check_sum == n

final_sum = 0

for j in range(10, 2540161):
    if fact_sum(j): final_sum += j

print(final_sum)