li = [i for i in range(13)]

for i in li:
    num1 = [2, 6, i, 9, 8]
    res1 = 0
    num2 = [4, i, 2, 9, 6]
    res2 = 0

    p = 0
    for a1 in num1[::-1]:
        res1 += (a1 * (13 ** p))
        p += 1

    p = 0
    for a2 in num2[::-1]:
        res1 += (a2 * (13 ** p))
        p += 1

    if (res1 + res2) % 34 == 0:
        print(i)
        break