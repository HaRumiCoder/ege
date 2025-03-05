def F(a):
    work = True
    for x in range(100):
        for y in range(100):
            if not (((3*x) + (4*y)) != 60 or ((a >= x) and (A >= y))):
                work = False
    return work

for A in range(200, 0, -1):
    if not (F(A)):
        print(A+1)
        break