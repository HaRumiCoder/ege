

res = 0

with open('for11') as f:
    for i in f.readlines():
        info = {}
        a = i.strip().split('\t')
        for j in a:
            info[int(j)] = (info.get(int(j)) or 0) + 1
        nums = list(info.values())
        nums.sort()
        if nums == [1, 1, 1, 2, 2]:
            povtor = dict(filter(lambda x: x[1] > 1, info.items()))
            unique = dict(filter(lambda x: x[1] == 1, info.items()))
            if sum(unique.keys()) / 3 >  sum(povtor.keys()) / 2:
                res += 1

print(res)
