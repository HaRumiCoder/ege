from itertools import product

nechet = '1357'
chet = '2468'
res = 0

for i in product(nechet,chet,nechet,chet,nechet,chet,nechet,chet,nechet,chet,nechet):
    num = ''.join(i)
    add = True
    for i in range(11):
        if num.count (num[i]) > 4:
            add = False
    if add:
        res += 1

print(res * 2)