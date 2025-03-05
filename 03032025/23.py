def f(n):
    if n == 25:
        return 1
    if n == 24:
        return 0
    if n > 25:
        return 0
    return f(n+1) + f(2*n + 1)

print(f(1))