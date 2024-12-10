minn = 1000000000

for x in range(12):
    for y in range(12):
        a1 = [x, 2, 3, 1, y]
        a = 0
        p = 0
        for i in a1[::-1]:
            a += i * (12 ** p)
            p += 1

        b1 = [7, 8, x, 9, 8, y]
        b = 0
        p = 0
        for i in b1[::-1]:
            b += i * (14 ** p)
            p += 1

        if (a + b) % 99 == 0:
            if (a + b) // 99 < minn:
                minn =  (a + b) // 99

print(minn)