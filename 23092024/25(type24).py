from itertools import product

b = "QRS"
with open('for25') as f:
    a = f.readline()

maxx = 0
res = 0
for i in range(len(a)):
    if a[i] in b and a[i+1] in b:
        res += 1
        if res > maxx:
            maxx = res
        res = 0
        continue
    res += 1

print(maxx)


