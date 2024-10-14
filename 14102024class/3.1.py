from itertools import product

n = list("КОМПЬТЕР")
n.sort()
li = list(product(n, repeat=5))
res = 0

for i in li:
    if 'К' not in i and i.count('Р') == 2:
        res = li.index(i) + 1

print(res)