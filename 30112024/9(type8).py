res = 0

for a1 in range(1, 9):
    for a2 in range(0, 9):
        for a3 in range(0, 9):
            for a4 in range(0, 9):
                for a5 in range(0, 9):
                    num = [a1, a2, a3, a4, a5]
                    if a1 == 2:
                        if a2 % 2 == 1:
                            continue
                    if a5 == 2:
                        if a4 % 2 == 1:
                            continue
                    can = True
                    for i in range(1, 4):
                        if num[i] == 2:
                            if num[i-1] % 2 == 1 or num[i+1] % 2 == 1:
                                can = False
                    if not can:
                        continue
                    if num.count(3) != 2:
                        continue
                    print(*num, sep='')
                    res += 1

print(res)