a = []
minn = 100000000
res = []

with open('for17') as f:
    for i in f.readlines():
        num = int(i.strip())
        a.append(num)
        if num % 10 == 5:
            if num < minn:
                minn = num

for i in range(len(a)-1):
    if [len(str(a[i])), len(str(a[i+1]))].count(3) != 1:
        continue
    if sum([a[i], a[i+1]]) % minn == 0:
        res.append(sum([a[i], a[i+1]]))

print(len(res), min(res))

