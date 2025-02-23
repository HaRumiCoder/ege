def F(n):
    if n < 9:
        return n
    return F(n % 9) + F(n // 9)

