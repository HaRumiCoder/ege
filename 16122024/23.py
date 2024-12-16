def F(a, is8=False):
    if a == 15:
        if is8:
            return 1
        return 0
    if a > 15:
        return 0
    if a == 8:
        is8 = True
    return F(a+1, is8) + F(a+2, is8) + F(a+3, is8)

print(F(1))