from itertools import permutations

n = list("ГЕРАСИМ")
n.sort()
li = list(permutations(n, 7))
res = []

glas = 'ЕА'
soglas = 'ГРСМ'

for i in li:
    addd = False
    for a in range(6):
        if (i[a] in glas and i[a+1] in glas) or (i[a] in soglas and i[a+1] in soglas):
            addd = False
            break
        else:
            addd = True
    if addd:
        res.append(i)

print(len(set(res)))

