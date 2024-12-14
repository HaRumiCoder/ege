res = 0

for a1 in range(1, 4):
    for a2 in range(4):
        for a3 in range(4):
            if a1 + a3 > a2:
                res += 1

print(res)