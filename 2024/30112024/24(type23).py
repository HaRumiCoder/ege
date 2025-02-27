def F(a, is33=False):
    if a == 5:
        if is33:
            return 1
        return 0
    if a < 5:
        return 0
    if a == 33:
        is33 = True
    return F(a-1, is33) + F(a//3, is33)

print(F(67))