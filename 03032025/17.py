a = []
res = []

with open('for17') as f:
    for i in f.readlines():
        a.append(int(i.strip()))

for i in range(len(a)-1):
    if a[i+1] - a[i] % 2 == 1:
        continue
    if a[i+1] % 31 == 0 or a[i] % 31 == 0:
        res.append(sum(a[i:i+2]))

print(len(res), max(res))