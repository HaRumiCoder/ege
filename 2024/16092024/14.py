for x in range(7):
    for y in range(7):
        num1 = [y, x, 3, 2, 0]
        res1 = 0
        num2 = [1, x, 3, y, 3]
        res2 = 0

        p = 0
        for a1 in num1[::-1]:
            res1 += (a1 * (7 ** p))
            p += 1

        p = 0
        for a2 in num2[::-1]:
            res1 += (a2 * (9 ** p))
            p += 1

        if (res1 + res2) % 181 == 0:
            print((res1 + res2) // 181)
            break

