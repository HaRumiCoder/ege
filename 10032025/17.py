a = []
maxx = 0
res = []
with open('for17') as f:
    for i in f.readlines():
        n = int(i.strip())
        a.append(n)
        if n % 1000 == 321 and n > maxx:
            maxx = n


for i in range(len(a)-2):
    if [len(str(j)) for j in a[i:i+3]].count(5) != 2:
        continue
    if [j%5 for j in a[i:i+3]].count(0) == 0:
        continue
    if sum(a[i:i+3]) <= maxx:
        continue
    res.append(sum(a[i:i+3]))

print(len(res), max(res))