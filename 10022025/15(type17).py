a = []
res  =[]

with open('for15') as f:
    for i in f.readlines():
        a.append((int(i.strip())))


minn_ost = min(a) % 5
maxx_ost = max(a) % 7

for i in range(len(a)-2):
    if 4 not in [len(str(a[j])) for j in range(i, i+3)]:
        continue
    if [a[j] % 5 for j in range(i, i+3)].count(minn_ost) > 1:
        continue
    if [a[j] % 7 for j in range(i, i + 3)].count(maxx_ost) < 2:
        continue
    res.append(sum(a[i:i+3]))

print(len(res), max(res))