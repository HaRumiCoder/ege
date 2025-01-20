def F(a, is14=False):
    if a == 28:
        if is14:
            return 1
        return 0
    if a > 28:
        return 0
    if a == 14:
        is14 = True
    return F(a+1, is14) + F(a*2, is14) + F(a*3, is14)

print(F(2))