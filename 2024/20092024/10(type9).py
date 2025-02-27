res = 0

with (open('for10') as f):
    for i in f:
        a = list(map(int, i.strip().split('\t')))
        if a.count(min(a)) != 1:
            continue
        if len(set(a)) == len(a):
            continue
        maxx = max(a)
        a.remove(maxx)
        if maxx / (sum(a) / len(a)) > 3:
            res += 1


print(res)

