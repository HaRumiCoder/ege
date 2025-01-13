res = 0

with open('for9') as f:
    for i in f.readlines():
        a = list(map(int, i.strip().split()))
        add = False
        for j in a:
            b = a[:]
            b.remove(j)
            print(b)
            if b[0] + b[1] > j:
                add = True
            if b[2] + b[1] > j:
                add = True
        if add:
            res += 1

print(res)

