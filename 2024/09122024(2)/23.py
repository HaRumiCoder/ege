def F(a, is10=False):
    if a == 14:
        if is10:
            return 1
        return 0
    if a > 14:
        return 0
    if a == 10:
        is10 = True
    return F(a+1, is10) + F(a*2, is10) + F(a+3, is10)

print(F(2))