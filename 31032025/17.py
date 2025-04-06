a = []

with open('for17') as f:
    for i in f.readlines():
        a.append(int(i.strip()))

res = []

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i] - a[j]) % 36 != 0:
            continue
        if (a[i] % 13 == 0) or (a[j] % 13 == 0):
            res.append(abs(a[i] - a[j]))

print(len(res), max(res))