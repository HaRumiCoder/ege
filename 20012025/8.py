res = 0

for a1 in range(1, 7):
    for a2 in range(7):
        for a3 in range(7):
            for a4 in range(7):
                n = [a1, a2, a3, a4]
                if list(set(n))[::-1] == n:
                    res += 1

print(res)