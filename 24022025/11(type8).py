from itertools import *

res = []

for i in product('КОНФТА', repeat=3):
    for j in permutations(''.join(i)+'ЕЕ', 5):
        if j[1] != 'Ф':
            res.append(j)

print(len(set(res)))
