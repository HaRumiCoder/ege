res = 0
with open('for6') as f:
    for s in f:
        a = list(map(int,s.strip().split('\t')))
        a.sort()
        if a[0]**2 + a[1]**2 > a[2]**2:
            res += 1
print(res)