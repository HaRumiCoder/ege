def F(n, is16=False):
    if n == 2:
        if is16:
            return 1
        return 0
    if n < 2:
        return 0
    if n == 16:
        is16 = True
    return F(n-2, is16) + F(n//2, is16)

print(F(38))