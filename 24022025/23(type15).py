for A in range(200):
    work = False
    for x in range(1, 200):
        for y in range(1, 200):
            if not ( ((y + (2*x)) > 48) or (y > x) or (x + (3*y) < A) ):
                print(A, x, y)
                work = True
    print(A, work)
    if not work:
        print(A-1)
        break