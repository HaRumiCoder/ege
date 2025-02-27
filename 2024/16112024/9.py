res = 0

with (open('for9') as f):
    for i in f:
        a = i.strip().split('\t')
        info = {}
        for j in a:
            info[int(j)] = (info.get(int(j)) or 0) + 1
        povtor = dict(filter(lambda x: x[1] > 1, info.items()))
        uniq = dict(filter(lambda x: x[1] == 1, info.items()))
        if len(povtor) != 1 or len(uniq) != 3:
            continue
        if (list(povtor.keys())[0] * 3) ** 2 > sum(uniq.keys()) ** 2:
            res += 1

print(res)