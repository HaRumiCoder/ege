for x in range(1, 15):
    a0 = [1, 2, 3, x, 5]
    a = 0
    p = 0
    for i in a0[::-1]:
        a += (i * (15 ** p))
        p += 1

    b0 = [1, x, 2, 3, 3]
    b = 0
    p = 0
    for i in b0[::-1]:
        b += (i * (15 ** p))
        p += 1

    if (a + b) % 14 == 0:
        print((a + b) // 14)