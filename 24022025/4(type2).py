from itertools import *

def f(x, y, z, w):
    return (x <= (y <= z)) and (y <= (z == (not(w))))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(0, 0, a1, 0), (0, 0, a2, a3), (a4, 0, a5, a6)]
    if len(tab) == len(set(tab)):
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, r))) for r in tab] == [0, 0, 0]:
                print(i)