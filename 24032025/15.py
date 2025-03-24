res = []

for A in range(200, 0, -1):
    work = True
    for m in range(100):
        for n in range(100):
            if not ( (((3 * m) + (4 * n)) > 66) or (m <= A) or (n < A) ):
                work = False
    if work:
        res.append(A)

print(min(res))
