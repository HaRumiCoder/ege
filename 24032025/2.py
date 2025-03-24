from itertools import product, permutations

def F(x, y, z, w):
    return ( ((z <= w) or (y == w)) and ((x or z) == y) )

for a1, a2, a3, a4 in product([1, 0], repeat=4):
    tab = ((0, 1, 1, 0), (a1, 1, 0, a2), (0, a2, a3, 1))
    if len(tab) == len(list(set(tab))):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                print(p)



