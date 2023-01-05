import time
import matplotlib.pyplot as plt

i = 2
fibs = [1, 1]
while len(str(fibs[-1])) < 1000:
    fibs.append(fibs[i-2]+fibs[i-1])
    i += 1
print(len(fibs))
