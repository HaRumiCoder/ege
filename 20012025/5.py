def F(N):
    n = bin(N)[2:]
    n = int(n[::-1])

    res = 0
    p = 0
    for i in str(n)[::-1]:
        res += int(i) * (2 ** p)
        p += 1

    return res


for i in range(100, 1, -1):
    if F(i) == 13:
        print(i)
        break