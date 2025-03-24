fileinfo = {}
lines = []

with open('for9') as f:
    for i in f.readlines():
        n = i.strip().split('\t')
        n = list(map(int, n))
        lines.append(n)
        for a in n:
            fileinfo[a] = (fileinfo.get(a) or 0) + 1
print(fileinfo)
res = 0

for line in lines:
    sr = sum(line) / len(line)
    interesting = 0
    for a in line:
        if line.count(a) != 1:
            continue
        if not (fileinfo[a] > 335):
            continue
        if a >= sr:
            continue
        interesting += 1
    if interesting == 1:
        res += 1

print(res)