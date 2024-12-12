for x in range(10000):
    a = 3 ** 100 - x

    res = ''
    while a >= 3:
        res += str(a % 3)
        a //= 3
    res += str(a)
    res = res[::-1]

    if res.count('0') == 2:
        print(x)
        break