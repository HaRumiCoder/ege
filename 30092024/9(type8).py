li = ['З', 'И', 'М', 'А']

glas = 'ИА'

res = 0

for a1 in li:
    for a2 in li:
        for a3 in li:
            for a4 in li:
                for a5 in li:
                    c = 0
                    for a in [a1, a2, a3, a4, a5]:
                        if a in glas:
                            c += 1
                    if c != 1:
                        continue

                    res += 1

print(res)