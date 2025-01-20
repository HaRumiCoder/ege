res = 0

with open('for9') as f:
    for i in f.readlines():
        a = i.strip().split()
        info = {}
        for j in a:
            info[int(j)] = (info.get(int(j)) or 0) + 1
        if not (list(info.values()).count(2) == 2 and list(info.values()).count(1) == 3):
            continue
        if (sum([x[0] for x in info.items() if x[1] == 1]) / 3) < (sum([x[0] for x in info.items() if x[1] == 2]) / 2):
            res += 1

print(res)