res = 0

for a1 in range(1, 8):
    for a2 in range(0, 8):
        for a3 in range(0, 8):
            for a4 in range(0, 8):
                for a5 in range(0, 8):
                    n = [a1, a2, a3, a4, a5]
                    if n.count(6) != 1:
                        continue
                    indexx = n.index(6)
                    if indexx == 0:
                        if n[indexx+1] % 2 != 1:
                            res += 1
                    if indexx == 4:
                        if n[indexx - 1] % 2 != 1:
                            res += 1
                    if 1 <= indexx <= 3:
                        if n[indexx + 1] % 2 != 1 and n[indexx-1] % 2 != 1:
                            res += 1


print(res)


print(res)