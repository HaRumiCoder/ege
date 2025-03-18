a = []
res = []

with open('for16') as f:
    for i in f.readlines():
        a.append(int(i.strip()))

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[j] - a[i]) % 60 != 0:
            continue
        if a[j] % 15 == 0 or a[i] % 15 == 0:
            res.append(a[i] - a[j])

print(len(res), max(res))