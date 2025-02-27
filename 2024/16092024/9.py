f = open('for9')
res = 0
for i in f:
    info = {}
    for j in i.strip().split('\t'):
        num = int(j)
        info[num] = (info.get(num) or 0) + 1
    if set(info.values()) == {1}:
        continue
    if info[max(info)] > 1:
        continue
    if sum([x * y for x, y in filter(lambda x: x[1] > 1, info.items())]) >= max(info):
        continue
    res += 1

print(res)
