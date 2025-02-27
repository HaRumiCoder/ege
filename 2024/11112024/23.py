def F(a, is11=False, is9=False):
    if a == 12:
        if is11 and is9:
            return 1
        return 0
    if a > 12:
        return 0
    if a == 11:
        is11 = True
    if a == 9:
        is9 = True
    return F(a+1, is11, is9) + F(a*3, is11, is9) + F(a+2, is11, is9)

print(F(2))