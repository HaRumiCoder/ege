def f(n, is14=False):
    if n == 62:
        if is14:
            return 1
        return 0
    if n > 62:
        return 0
    if n == 59:
        return 0
    if n == 14:
        is14 = True
    return f(n+1, is14) + f(n*2, is14)

print(f(3))