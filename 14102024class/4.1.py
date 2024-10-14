from itertools import product

n = list('АБЗИ')
n.sort()
li = ['0'] + list(''.join(i) for i in product(n, repeat=4))
print(li.index('ИЗБА'))