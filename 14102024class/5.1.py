from itertools import product

n = list('АЛГОРИТМ')
n.sort()
li = list(product(n, repeat=4))

res = 0

for i in li:
    res += 1
    print(i[:2])
    if i[:2] == ('И', 'Г'):
        print(res)
        break

