from itertools import *

def f(x, y, z, w, u):
    return ((z <= w) and (y == (not (x)))) <= (u == (y or z))

for a1, a2, a3, a4, a5, a6, a7, a8 in product([1,0], repeat=8):
    tab = [(0, a1, 0, 0, 0), (0, a2, a3, 0, 0), (a4, 0, 0, 0, a5), (0, 0, a6, a7, a8)]
    if len(tab) == len(set(tab)):
        for i in permutations('xyzwu'):
            if [f(**dict(zip(i, r))) for r in tab] == [0, 0, 0, 0]:
                print(i)