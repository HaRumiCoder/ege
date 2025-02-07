def F(N):
    n = str(bin(N))[2:]

    for i in range(2):
        num = list(map(int, n))
        n += str(sum(num) % 2)

    res = 0
    p = 0

    for i in n[::-1]:
        res += (2 ** p) * int(i)
        p += 1

    return res


for i in range(1000):
    if F(i) > 123:
        print(F(i))
        break
