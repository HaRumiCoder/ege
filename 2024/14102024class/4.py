n = list('АБЗИ')
n.sort()
res = 0
for a1 in n:
    for a2 in n:
        for a3 in n:
            for a4 in n:
                res += 1
                if a1 + a2 + a3 + a4 == 'ИЗБА':
                    print(res)