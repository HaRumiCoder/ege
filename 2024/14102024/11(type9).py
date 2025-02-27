res = 0

with open('for12') as f:
    for i in f.readlines():
        n = list(map(int, i.strip().split('\t')))
        n.sort()
        if len(set(n)) != 5:
            continue
        print(n)
        for a in set(n):
            if n.count(a) == 2:
                povtor = a
        n.remove(povtor)
        n.remove(povtor)
        print(n)
        if povtor < (sum(n) / 4):
            res += 1


print(res)

