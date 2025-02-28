for x in range(1, 9):
    for y in range(9):
        num1 = 0
        p = 0
        for i in [2, y, 6, 6, x][::-1]:
            num1 += (i * (9 ** p))
            p += 1

        num2 = 0
        p = 0
        for i in [x, 0, y, 1][::-1]:
            num2 += (i * (12 ** p))
            p += 1

        if (num1 + num2) % 170 == 0:
            print((num1 + num2) // 170)
            break