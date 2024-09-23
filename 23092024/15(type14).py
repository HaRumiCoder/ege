for x in range(0, 11):

    a = [2, 8, x, 2]
    b = [9, 3, x, 5]

    a1 = 0
    p = 0
    for i in a[::-1]:
        a1 += i * (18 ** p)
        p += 1

    b1 = 0
    p = 0
    for i in b[::-1]:
        b1 += i * (12 ** p)
        p += 1

    print(a1, b1)
    if (a1 + b1) % 133 == 0:
        print((a1 + b1) // 133)
        break
