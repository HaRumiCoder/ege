res = 0

with open('for10') as f:
    for i in f:
        a = list(map(int, i.strip().split('\t')))
        a.sort()
        if a[-1] >= sum(a[:-1]):
            continue
        if not ((a[0] + a[2] == a[1] + a[3]) or (a[0] + a[3] == a[2] + a[1])):
            continue
        res += 1

print(res)
