with open('for7') as f:
    res = 0
    for s in f:
        a = list(map(int, s.strip().split('\t')))
        if len(set(a)) == len(a):
            if (min(a) + max(a)) / 2 > (sum(a) - max(a) - min(a))/4:
                res += 1

print(res)
