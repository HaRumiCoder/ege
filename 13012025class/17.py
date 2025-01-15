maxx = 0
a = []
max_sum = 0
res = 0

with open('for17') as f:
    for i in f.readlines():
        n = i.strip().split('\t')[0]
        if len(n) == 0:
            continue
        if n[-1] == '3' and int(n) > maxx:
            maxx = int(n)
        a.append(n)

for i in range(len(a)-1):
    if (a[i][-1] == '3' and a[i+1][-1] != '3') or  (a[i+1][-1] == '3' and a[i][-1] != '3'):
        if int(a[i])**2 + int(a[i+1])**2 >= (maxx ** 2):
            if int(a[i])**2 + int(a[i+1])**2 > max_sum:
                max_sum = int(a[i]) ** 2 + int(a[i + 1]) ** 2
            res += 1

print(res, max_sum)