def F(a, is12=False):
    if a == 3:
        if is12:
            return 1
        return 0
    if a < 3:
        return 0
    if a == 12:
        is12 = True
    return F(a-2, is12) + F(a//3, is12) + F(a//2, is12)

print(F(38))