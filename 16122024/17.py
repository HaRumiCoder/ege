a = []
res = 0
maxx = 0

with open('for17') as f:
    for i in f.readlines():
        n = int(i.strip().split('\t')[0])
        a.append(n)

for i in range(len(a)-1):
    if a[i] % 160 != a[i+1] % 160:
        if a[i] % 7 == 0 or a[i+1] % 7 == 0:
            res += 1
            if a[i] + a[i+1] > maxx:
                maxx = a[i] + a[i+1]

print(res, maxx)