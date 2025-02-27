minn = 1000000000

for x in range(9):
    for y in range(9):
        a1 = [8, 8, x, 4, y]
        a = 0
        p = 0
        for i in a1[::-1]:
            a += i * (9 ** p)
            p += 1

        b1 = [7, x, 4, 4, y]
        b = 0
        p = 0
        for i in b1[::-1]:
            b += i * (11 ** p)
            p += 1

        if (a + b) % 61 == 0:
            if (a + b) // 61 < minn:
                minn =  (a + b) // 61

print(minn)