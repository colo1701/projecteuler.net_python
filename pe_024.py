import numpy as np
from itertools import permutations

perms = np.array(list(permutations([0,1,2,3,4,5,6,7,8,9])))
print(perms[999999])
