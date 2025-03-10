from itertools import product
res = 0

for p in product('АНДРЕЙ', repeat=6):
    if p.count('А') < 1:
        continue
    if p.count('Й') > 1:
        continue
    res += 1

print(res)