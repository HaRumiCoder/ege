for A in range(100, 0, -1):
    A_True = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not ((((3 * x) + (5 * y)) < A) + (x >= y) + (y > 8)):
                A_True = False
                break
        if not A_True:
            break
    if A_True:
        print(A)
