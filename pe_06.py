def square_of_sum(N):
    return sum(range(N+1))**2

def sum_of_squares(N):
    sos = 0
    for i in range(N+1): sos += i**2
    return sos

print(square_of_sum(100)-sum_of_squares(100))