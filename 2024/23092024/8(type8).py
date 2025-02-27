res = 0
for a1 in range(1, 9):
    for a2 in range(9):
        for a3 in range(9):
            for a4 in range(9):
                for a5 in range(9):
                    n = [a1, a2, a3, a4, a5]
                    if n.count(5) == 1:
                        a = n.index(5)
                        if 1 <= a <= 3:
                            if n[a-1] % 2 == 0 and n[a+1] % 2 == 0:
                                res += 1
                        elif a == 0:
                            if n[a + 1] % 2 == 0:
                                res += 1

                        elif a == 4:
                            if n[a - 1] % 2 == 0:
                                res += 1

print(res)