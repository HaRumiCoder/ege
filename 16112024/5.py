b = 0

for i in range(456789011, 123456789, -1):
    n = list(map(int, str(bin(i))[2:]))
    if n[-1] % 2 != 0:
        n.insert(0, 1)
        n.append(1)
        n.append(0)

    res = 0
    p = 0
    for j in n[::-1]:
        res += j * (2**p)
        p += 1

    print(res)
    break
