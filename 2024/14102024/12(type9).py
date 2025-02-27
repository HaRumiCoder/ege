res = 0

with open('for12') as f:
    for i in f.readlines():
        i = list(map(int, i.strip().split('\t')))
        i.sort()
        if i[-1] > sum(i[:-1]) and len(i) == 4:
            res += 1

print(res)