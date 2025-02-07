for A in range(1000, 1, -1):
    work = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not ((x * y < A) or (x < y) or (x >= 12)):
                work = False
    if not work:
        print(A+1)
        break