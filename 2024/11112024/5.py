maxx = 0

for i in range(1000000, 0, -1):
    n = str(bin(i))[2:]
    if i % 5 == 0:
        n += str(bin(5))[2:]
    else:
        n += '1'

    res0 = 0
    p = 0
    for j in n[::-1]:
        res0 += int(j) * (2 ** p)
        p += 1

    if res0 % 7 == 0:
        n += str(bin(7))[2:]
    else:
        n += '1'

    res = 0
    p = 0
    for j in n[::-1]:
        res += int(j) * (2 ** p)
        p += 1

    if res < 1728404:
        print(i)
        break