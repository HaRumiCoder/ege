def F(n, is14=False):
    if n == 50 and is14:
        return 1
    if n >= 50:
        return 0
    if n == 16:
        return 0
    if n == 14:
        is14 = True
    return F(n+1, is14) + F(n*2, is14) + F(n*3, is14)

print(F(1))