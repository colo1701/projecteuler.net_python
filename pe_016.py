def quers(n):
    qsum = 0
    for i in str(n): qsum += int(i)
    return qsum

quers(2**1000)
