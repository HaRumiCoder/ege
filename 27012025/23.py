def F(n, is12=False):
    if n > 16:
        return 0
    if n == 16:
        if is12:
            return 1
    if n == 12:
        is12 = True
    return F(n+1, is12) + F(n+3, is12) + F(n*2, is12)

print(F(3))