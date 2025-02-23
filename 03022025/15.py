for A in range(1, 100):
    work = True
    for x in range(1, 200):
        for y in range(1, 200):
            if not ( ((y + (2*x)) != 48) or (A < x) or (A < y) ):
                print(A, x, y)
                work = False
    print(A, work)
    if not work:
        print(A-1)
        break