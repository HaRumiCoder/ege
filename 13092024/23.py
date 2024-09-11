def F(x):
    if x == 31:
        return 1
    if 31 - x < 10:
        return F(x+1)
    return F(x+1) + F(x+10)

print(F(10))