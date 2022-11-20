import time

zahl = 600851475143
teiler = 3
primefacts = []

while True:
    if zahl%teiler == 0:
        zahl /= teiler
        primefacts.append(teiler)
    teiler += 2
    if teiler > zahl:
        break

print(primefacts[-1])