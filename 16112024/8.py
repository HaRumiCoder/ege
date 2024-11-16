a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15]

res = 0

for a1 in a[1:]:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        for a7 in a:
                            for a8 in a:
                                n = [a1, a2, a3, a4, a5, a6, a7, a8]
                                if n.count(0) != 0:
                                    continue
                                if len(list(filter(lambda x: x>=10, n))) > 4:
                                    continue
                                res += 1

print(res)