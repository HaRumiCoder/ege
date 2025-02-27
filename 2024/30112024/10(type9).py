res = 0

with (open('for10') as f):
    for i in f:
        a = i.strip().split('\t')
        info = {}
        for j in a:
            info[int(j)] = (info.get(int(j)) or 0) + 1
        povtor = dict(filter(lambda x: x[1] > 1, info.items()))
        uniq = dict(filter(lambda x: x[1] == 1, info.items()))
        print(povtor)
        if not(len(povtor) == 1 and list(povtor.items())[0][1] == 3):
            continue
        if sum(value * 3 for value, num in povtor.items())**2  > sum(value for value, num in uniq.items())**2:
            res += 1

print(res)