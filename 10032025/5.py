def f(n):
    n = str(n)
    res = [int(n[0]) + int(n[1]), int(n[1]) + int(n[2])]
    res.sort()
    return str(res[0]) + str(res[1])

for i in range(100, 1000):
    if f(i) == '714':
        print(i)
        break