from itertools import permutations

n = list("РОСОМАХА")
n.sort()
li = list(permutations(n, 8))
res = []

glas = 'ОА'
soglas = 'РСМХ'

for i in li:
    addd = False
    for a in range(7):
        if (i[a] in glas and i[a+1] in glas) or (i[a] in soglas and i[a+1] in soglas):
            addd = False
            break
        else:
            addd = True
    if addd:
        res.append(i)

print(len(set(res)))
