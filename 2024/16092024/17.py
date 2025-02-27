f = open('for17')

res = []

li = []
for i in f:
    li.append(int(i.strip()))

li = list(set(li))


for i in range(len(li)):
    for j in range(i+1, len(li)):
        if (li[i] + li[j]) % 120 == 0:
            res.append((li[i], li[j]))

res = list(sorted(res, key=lambda x: x[0] + x[1], reverse=True))

print(len(res), sum(res[0]))