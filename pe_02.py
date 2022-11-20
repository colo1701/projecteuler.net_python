def fib(limit):
    fib_list = [1, 2]
    while fib_list[-1] <= limit: fib_list.append(fib_list[-2]+fib_list[-1])
    fib_list.pop()
    return fib_list

def even_count(N):
    counter = 0
    for i in fib(N):
        if i%2 == 0: counter += i
    return counter

even_count(4000000)