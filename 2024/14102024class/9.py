n1 = 'МАТВЕ'
n2 = 'МАТВЕЙ'

res = 0
for a1 in n1:
    for a2 in n2:
        for a3 in n2:
            for a4 in n2:
                for a5 in n2:
                    for a6 in n2:
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if 'АЕ' in word:
                            continue
                        if len(set(word)) != 6:
                            continue
                        res += 1


print(res)