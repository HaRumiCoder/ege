for x in range(18, -1, -1):

    a = [9, 8, 8, 9, 7, x, 2, 1]
    b = [2, x, 9, 2, 3]

    a1 = 0
    p = 0
    for i in a[::-1]:
        a1 += i * (19 ** p)
        p += 1

    b1 = 0
    p = 0
    for i in b[::-1]:
        b1 += i * (19 ** p)
        p += 1

    print(a1, b1)
    if (a1 + b1) % 18 == 0:
        print((a1 + b1) // 18)
        break
