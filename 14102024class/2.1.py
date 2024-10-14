from itertools import product, combinations, permutations
n = list('ВЕРОНИКА')
n.sort()

res = 0

for a in list(product(n, repeat=3)):
    if a.count('В') != 1:
        continue
    print(a)
    res += 1
    if 'А' not in a:
        print(res)
        break