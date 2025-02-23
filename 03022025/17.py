a = []
maxx13 = 0
res = []


with open('for17') as f:
    for i in f.readlines():
        num = int(i.strip())
        if num % 100 == 13:
            if num > maxx13:
                maxx13 = num
        a.append(int(i.strip()))


for i in range(len(a)-2):
    if [len(str(j)) for j in a[i:i+3]].count(3) != 2:
        continue
    if sum(a[i:i+3]) > maxx13:
        continue
    res.append(sum(a[i:i+3]))

print(len(res), max(res))