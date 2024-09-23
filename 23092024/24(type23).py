def F(n):
    if n > 93:
        return 0
    if n == 93:
        return 1
    if (93 / n) > 3:
        return F(n * 3) + F(n + 3)
    return F(n + 3)

print(F(3))