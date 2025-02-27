a = []

with open('for18') as f:
    for i in f.readlines():
        a.append(int(i.strip()))

maxx = 0
res = 0


for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if (a[i] + a[j]) % 126 == 0:
            res += 1
            s = (a[i] + a[j])
            if s > maxx:
                maxx = s

print(res, maxx)
