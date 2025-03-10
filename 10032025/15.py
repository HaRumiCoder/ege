res = []

for A in range(1, 100):
    work = True
    for x in range(1, 100):
        if not ((120 % A == 0) and ((x % A != 0) <= ((x % 18 == 0) <= (x % 24 != 0)))):
            work = False
            break
    if work:
        res.append(A)


print(max(res))