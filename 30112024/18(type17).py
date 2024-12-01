a = []
num = 0
res = 0
maxx = 0

with open('for18') as f:
    for i in f.readlines():
        n = int(i.strip().split('\t')[0])
        if n % 32 == 0:
            num += 1
        a.append(n)

for i in range(len(a)-1):
    if (a[i] < 0 or a[i+1] < 0) and a[i] + a[i+1] < num:
        res += 1
        if a[i] + a[i+1] > maxx:
            maxx = a[i] + a[i+1]

print(res, maxx)
