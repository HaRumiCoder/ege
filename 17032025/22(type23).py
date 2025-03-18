def F(n, is18=False):
    if n > 37:
        return 0
    if n == 37:
        if is18:
            return 1
    if n == 18:
        is18 = True
    return F(n+1, is18)+ F(n*2, is18)

print(F(3))