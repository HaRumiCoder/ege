def F(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x % 2 == 1:
        return (7*x + F(x-1) - F(x-2)) // 5
    return (3*x + F(x-3)) // 3

print(F(35))