a = []
minn = 10000000
res = []

with open('for17') as f:
    for i in f.readlines():
        num = int(i.strip())
        a.append(num)
        if num % 21 == 0:
            if num < minn:
                minn = num

for i in range(len(a) - 1):
    if a[i] % minn == 0 or a[i+1] % minn == 0:
        res.append(a[i] + a[i+1])

print(len(res), max(res))

