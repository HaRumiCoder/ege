for x in range(15):
    for y in range(15):
        num1 = 0
        p = 0
        for i in [9, 0, x, 4, y][::-1]:
            num1 += (i * (15 ** p))
            p += 1

        num2 = 0
        p = 0
        for i in [9, 1, x, y, 2][::-1]:
            num2 += (i * (16 ** p))
            p += 1

        if (num1 + num2) % 56 == 0:
            print((num1 + num2) // 56)
            break