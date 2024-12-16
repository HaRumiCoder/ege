minn = 1000000000

for x in range(12):
    for y in range(12):
        a1 = [8, x, 7, 8, y]
        a = 0
        p = 0
        for i in a1[::-1]:
            a += i * (13 ** p)
            p += 1

        b1 = [7, 9, x, y, 7]
        b = 0
        p = 0
        for i in b1[::-1]:
            b += i * (14 ** p)
            p += 1

        if (a + b) % 9 == 0:
            if (a + b) // 9 < minn:
                minn =  (a + b) // 9

print(minn)