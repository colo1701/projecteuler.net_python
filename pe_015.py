import numpy as np

def nfac(n):
    return np.math.factorial(n)

def binco(n, k):
    return nfac(n)/(nfac(k)*nfac(n-k))

int(binco(40, 20))
