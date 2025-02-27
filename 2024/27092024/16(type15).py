stop = False

for A in range(100, 0, -1):
    for m in range(0, 100):
        for n in range(0, 100):
            if not ( ((3 * m) + (4 * n) > 63) + ((m <= A) * (n < A)) ):
                print(A + 1)
                stop = True
            if stop:
                break
        if stop:
            break