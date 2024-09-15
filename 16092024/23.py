def F(x):
    if x == 32:
        return 1
    if 32 - x < 10:
        return F(x+1)
    return F(x+1) + F(x+10)

print(F(10))