def F(n):
    if n < 3:
        return 1
    return sum(F(i) for i in range(n-1))


print(F(18))
