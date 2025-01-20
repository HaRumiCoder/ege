a = []
res = []
with open('for17') as f:
    for i in f.readlines():
        a.append(int(i.strip()))

for i in range(len(a)-1):
    if ((a[i] * a[i+1]) % 15 == 0) and ((a[i] + a[i+1]) % 7 == 0):
        res.append(a[i] + a[i+1])


print(len(res), max(res))