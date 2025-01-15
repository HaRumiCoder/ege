res = 0

with open('for9') as f:
    for i in f.readlines():
        a = list(map(int, i.strip().split()))
        a.sort()
        if a[0] + a[1] <= a[2] or a[0] + a[1] <= a[3] or a[1] + a[2] <= a[3]:
            res += 1

print(res)

