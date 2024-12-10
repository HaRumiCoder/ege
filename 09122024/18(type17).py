a = []
res = []
maxx = 0
maxx_res = 0

with open('for18') as f:
    for i in f.readlines():
        n = int(i.strip().split('\t')[0])
        if n % 100 == 17 and n > maxx:
            maxx = n
        a.append(n)

for i in range(len(a)-2):
    print(a[i:i+3])
    lengths = list(map(lambda x: len(str(x)), a[i:i+3]))
    if lengths.count(4) != 2:
        continue
    is5 = list(map(lambda x: x % 5, a[i:i+3]))
    if is5.count(0) == 0:
        continue
    if sum(a[i:i+3]) > maxx:
        res.append(sum(a[i:i+3]))

print(len(res), max(res))
