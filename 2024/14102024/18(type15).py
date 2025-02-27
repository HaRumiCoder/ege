stop = False

for A in range(100, 0, -1):
    for x in range(0, 100):
        for y in range(0, 100):
            if not (x<A) + (y<A) + (x + (2*y) > 50):
                print(A + 1)
                stop = True
            if stop:
                break
        if stop:
            break