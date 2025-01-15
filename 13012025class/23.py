def F(a, is11=False, is12=False):
    if a == 24:
        if (is11 and not is12) or (is12 and not is11):
            return 1
        return 0
    if a > 24:
        return 0
    if a == 11:
        is11 = True
    if a == 12:
        is12 = True
    return F(a+1, is11, is12) + F(a*2, is11, is12)

print(F(2))