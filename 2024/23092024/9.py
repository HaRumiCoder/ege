res = 0

with open('for9') as f:
    for i in f.readlines():
        a = list(map(int, i.strip().split('\t')))
        if len(set(a)) == 6:
            continue
        if a.count(max(a)) != 1:
            continue
        maxx = a.pop(a.index(max(a)))
        if (maxx / (sum(a) / 5)) > 3:
            res += 1

print(res)
