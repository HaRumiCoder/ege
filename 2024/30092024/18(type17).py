li = []

maxx = 0

with open('for18') as f:
    for i in f.readlines():
        li.append(int(i.strip()))

res = 0

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if (li[i] * li[j]) % 10 == 0:
            a = li[i] + li[j]
            res += 1
            if a > maxx:
                maxx = a

print(res, maxx)