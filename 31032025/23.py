def F(n, is15=False):
    if n == 50:
        if is15:
            return 1
    if n >= 50:
        return 0
    if n == 33:
        return 0
    if n == 15:
        is15 = True
    return F(n+1, is15) + F(n*2, is15) + F(n*3, is15)


print(F(3))


