import numpy as np

def build_matrix(n: int) -> list:
    M = np.zeros((n, n), np.int32)
    M[int(np.floor(len(M))/2), int(np.floor(len(M))/2)] = 1
    
    counter = 2
    lap = 0
    x, y = int(np.floor(len(M))/2), int(np.floor(len(M))/2)
    
    for i in range(int(np.floor(len(M))/2)):
        lap += 1
        
        x, y = x+1, y
        M[y, x] = counter
        counter += 1
        
        for j in range(2*lap - 1):
            x, y = x, y+1
            M[y, x] = counter
            counter += 1
        
        for k in range(2*lap):
            x, y = x-1, y
            M[y, x] = counter
            counter += 1
        
        for l in range(2*lap):
            x, y = x, y-1
            M[y, x] = counter
            counter += 1
        
        for m in range(2*lap):
            x, y = x+1, y
            M[y, x] = counter
            counter += 1
    return M

A = build_matrix(1001)

sum_diag, sum_anti = 0, 0

for a in range(len(A)):
    sum_diag += A[a, a]
    sum_anti += A[a, -(a+1)]

print(sum_diag + sum_anti - 1)
