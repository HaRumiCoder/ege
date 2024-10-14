res = 0

for a1 in range(1, 9):
    for a2 in range(0, 9):
        for a3 in range(0, 9):
            for a4 in range(0, 9):
                for a5 in range(0, 9):
                    n = [a1, a2, a3, a4, a5]
                    a = list(sorted(set(n), reverse=True))
                    if n == a:
                        res += 1

print(res)