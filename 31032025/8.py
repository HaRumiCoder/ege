from itertools import permutations

res = 0

for i in permutations('ОЛЬГА'):
    if i[0] == 'Ь':
        continue
    if i[i.index('Ь')-1] in 'ОА':
        continue
    res += 1

print(res)