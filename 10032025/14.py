for A in range(1, 1000):
    for x in range(9):
        M0 = [8, 4, 2, x, 5]
        p = 0
        M = 0
        for i in M0:
            M += (i * (9 ** p))
            p += 1

        N0 = [8, x, 7, 2, 5]
        p = 0
        N = 0
        for i in N0:
            N += (i * (9 ** p))
            p += 1

        if (M + A) % N == 0:
            print(A)
            break