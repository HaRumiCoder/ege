def F(n, isA=False):
    if n == 15:
        return 1
    if n > 16:
        return 0
    if isA:
        return F(n*2) + F(n*3)
    return F(n*2) + F(n*3) + F(n-1, isA=True)

print(F(3))