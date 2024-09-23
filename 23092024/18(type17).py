a = []
maxx = 0
res = 0
minn = 10000000

with open('for18') as f:
    for i in f:
        elem = int(i.strip())
        if elem % 100 == 24 and elem > maxx:
            maxx = elem
        a.append(elem)

print(maxx)
for a1 in range(len(a)-2):
    li = [a[a1], a[a1+1], a[a1+2]]
    print(li)
    length3 = 0
    for i in li:
        if len(str(i)) == 3:
            length3 += 1
    if length3 != 1:
        continue
    if sum(li) > maxx:
        res += 1
        if sum(li) < minn:
            minn = sum(li)

print(res, minn)
