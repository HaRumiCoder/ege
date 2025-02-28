a = []
res  =[]
maxx = 0

with open('for28') as f:
    for i in f.readlines():
        num = (int(i.strip()))
        if num % 1000 == 538 and num > maxx:
            maxx = num
        a.append(num)

print(maxx)

for i in range(len(a)-3):
    if [len(str(a[j])) for j in range(i, i+4)].count(5) < 2:
        continue
    if len(set([len(str(a[j])) for j in range(i, i+4)])) == 1:
        continue
    if [a[j] % 3 for j in range(i, i+4)].count(0) <= [a[j] % 7 for j in range(i, i+4)].count(0) :
        continue
    if sum(a[i:i+4]) <= maxx or sum(a[i:i+4]) >= (2 * maxx) :
        continue
    print(a[i:i+4])
    res.append(sum(a[i:i+4]))

print(len(res), max(res))