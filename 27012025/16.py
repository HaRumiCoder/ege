def F(n):
    if n == 0:
        return 0
    if n % 3 == 0:
        return F(n // 3)
    return (n % 3) + F(n - (n % 3))

for i in range(1000):
    if F(i) == 11:
        print(i)
        break