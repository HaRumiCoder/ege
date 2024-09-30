info = {}
lines = []


with open('for11') as f:
    for i in f.readlines():
        line = list(map(int, i.strip().split('\t')))
        for a in line:
            info[a] = (info.get(a) or 0) + 1
        lines.append(line)

res = 0

for line in lines:
    for a in line:
        if line.count(a) != 1:
            continue
        if info[a] == 46:
            res += 1
            break

print(res)