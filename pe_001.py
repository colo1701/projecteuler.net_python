def multiples3or5(N, counter = 0):
    for i in range(N):
        if i%3 == 0 or i%5 == 0: counter += i
    return counter

multiples3or5(1000)
