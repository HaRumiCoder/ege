a = []
res  =[]

with open('for16') as f:
    for i in f.readlines():
        a.append((int(i.strip())))


maxx_ost = max(a) % 7
minn_ost = min(a) % 3

for i in range(len(a)-1):
    if [a[j] % 3 for j in range(i, i+2)].count(minn_ost) < 1:
        continue
    if [a[j] % 7 for j in range(i, i + 2)].count(maxx_ost) < 1:
        continue
    res.append(sum(a[i:i+2]))

print(len(res), max(res))