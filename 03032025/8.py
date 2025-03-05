from itertools import product

res = 0
for p in product('БОРИС', repeat=6):
    if [p.count(i) for i in 'БР'] != [1, 1]:
        continue
    if p.count('С') > 1:
        continue
    res += 1
    print(p)

print(res)