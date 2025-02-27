for x in range(1, 8):
    for y in range(8):
        num1 = [x, 0, 1, y, 4]
        res1 = 0
        num2 = [x, y, 5, 4, 4]
        res2 = 0

        p = 0
        for a1 in num1[::-1]:
            res1 += (a1 * (9 ** p))
            p += 1

        p = 0
        for a2 in num2[::-1]:
            res1 += (a2 * (8 ** p))
            p += 1

        if (res1 + res2) % 89 == 0:
            print((res1 + res2) // 89)
            break

