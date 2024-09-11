f = open('for9')
res = 0
for i in f:
    line = list(map(int, i.strip().split('\t')))
    add = False
    print(line)
    for a1 in range(4):
        for a2 in range(4):
            for a3 in range(4):
                if line[a1] + line[a2] < line[a3]:
                    add = True
                if line[a2] + line[a3] < line[a1]:
                    add = True
                if line[a1] + line[a3] < line[a2]:
                    add = True
    if add:
        res += 1

print(res)