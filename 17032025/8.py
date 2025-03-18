from itertools import product
res = 0

for p in product('ABCDX', repeat=4):
    if p.count('X') != 1:
        continue
    res += 1

print(res)