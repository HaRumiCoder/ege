for x in range(13):
    A0 = [4, 12, x, 4]
    p = 0
    A = 0
    for i in A0[::-1]:
        A += (i * (15 ** p))
        p += 1

    B0 = [x, 6, 2, 10]
    p = 0
    B = 0
    for i in B0[::-1]:
        B += (i * (13 ** p))
        p += 1

    if (A + B) % 121 == 0:
        print((A + B) // 121)
        break