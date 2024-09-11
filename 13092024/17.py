f = open('for17')

li = []
minn = 100000000
for i in f:
    a = int(i.strip())
    if a % 5 == 0 and a < minn:
        minn = a
    li.append(a)

minn = minn**2
res = 0
maxx = 0

for i in range(len(li)-1):
    a1, a2 = int(li[i]), int(li[i+1])

    if min(a1, a2) % 5 == 0:
        summ = (a1**2) + (a2**2)
        if summ < minn:
            res += 1
            if summ > maxx:
                maxx = summ

print(res, maxx)
