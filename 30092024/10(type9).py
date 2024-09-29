res = 0

with open('for10') as f:
    for i in f:
        a = list(map(int, i.strip().split('\t')))
        a.sort()
        print(a)
        if len(set(a)) != 6:
            continue
        if (a[0] + a[-1]) / 2 > (sum(a[1:5]) / 4):
            res += 1

print(res)
