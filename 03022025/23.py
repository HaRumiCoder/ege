def f(n):
    if n == 20:
        return 1
    if n > 20:
        return 0
    return f(n+2) + f(n+5)

print(f(1))