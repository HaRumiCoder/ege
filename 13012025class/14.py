for x in range(1, 12):
    for y in range(1, 12):
        a = [y, 10, 10, x]
        a1 = 0
        p = 0
        for i in a[::-1]:
            a1 += i * (12**p)
            p += 1
        b = [x, 0, 2, y]
        b1 = 0
        p = 0
        for i in b[::-1]:
            b1 += i * (14 ** p)
            p += 1
        if (b1 + a1) % 80 == 0:
            print((b1 + a1) // 80)