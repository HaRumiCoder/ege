for x in range(15):
    num1 = 0
    p = 0
    for i in [6, 3, x, 5, 9, 6, 8, 5][::-1]:
        num1 += (i * (22 ** p))
        p += 1

    num2 = 0
    p = 0
    for i in [1, 7, x, 5, 3][::-1]:
        num2 += (i * (22 ** p))
        p += 1

    num3 = 0
    p = 0
    for i in [3, 6, x, 5][::-1]:
        num3 += (i * (22** p))
        p += 1

    if (num1 + num2 + num3) % 21 == 0:
        print((num1 + num2 + num3) // 21)
        break