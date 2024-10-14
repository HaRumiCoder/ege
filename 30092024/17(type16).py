def F(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return n + F(n-2)
    return n * F(n-1)

print(F(40))