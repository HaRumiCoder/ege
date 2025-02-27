from itertools import product

n = list("МАНГУСТ")
n.sort()
li = list(product(n, repeat=6))
res = 0

for i in li:
    if i[0] != 'У' and i.count('М') == 2 and i.count('Г') <= 1:
        res = li.index(i) + 1

print(res)