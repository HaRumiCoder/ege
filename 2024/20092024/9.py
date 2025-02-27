res = 0

with (open('for9') as f):
    for i in f:
        a = i.strip().split('\t')
        info = {}
        for j in a:
            info[int(j)] = (info.get(int(j)) or 0) + 1
        povtor = dict(filter(lambda x: x[1] > 1, info.items()))
        uniq = dict(filter(lambda x: x[1] == 1, info.items()))
        if not (povtor and uniq):
            continue
        if sum(value * num for value, num in uniq.items()) / sum(uniq.values()) > sum(value * num for value, num in povtor.items()) / sum(povtor.values()):
            res += 1

print(res)