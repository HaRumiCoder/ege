def F(x, m=True):
    if x == 11:
        return 1
    res = []
    if 11 - x >= 2:
        res.append(F(x+2))
    if 11 - (x * 2) >= 1 and m:
        res.append(F(x*2, m=False))
    res.append(F(x+1))
    return sum(res)

print(F(1))