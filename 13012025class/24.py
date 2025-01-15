
lines = []

with open('for24') as f:
    for a in f.readlines():
        if a.count('A') < 25:
            lines.append(a)

for line in lines:
    dictt = {}
    for i in range(len(line)):
        dictt[line[i]] = (dictt.get(line[i]) or []) + [i]

    res = []
    for i in dictt.values():
        res += [i[-1] - i[0]]

    print(max(res))