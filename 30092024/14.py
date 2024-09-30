minn = 1000000000

for x in range(11):
    for y in range(11):
        a1 = [x, 3, 4, 1, y]
        a = 0
        p = 0
        for i in a1[::-1]:
            a += i * (11 ** p)
            p += 1

        b1 = [5, 6, x, 1, y]
        b = 0
        p = 0
        for i in b1[::-1]:
            b += i * (19 ** p)
            p += 1

        if (a + b) % 305 == 0:
            if (a + b) // 305 < minn:
                minn =  (a + b) // 305

print(minn)