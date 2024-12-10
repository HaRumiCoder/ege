for i in range(34722200, 34733300):
    n = str(bin(i))[2:]
    n += str(bin(i%3))[2:]

    res0 = 0
    p = 0
    for j in n[::-1]:
        res0 += int(j) * (2 ** p)
        p += 1

    n += str(bin(res0 % 5))[2:]

    res = 0
    p = 0
    for j in n[::-1]:
        res += int(j) * (2 ** p)
        p += 1

    if res >= 1111111110:
        a = i
        break


for i in range(45000000, 50000000):
    n = str(bin(i))[2:]
    n += str(bin(i%3))[2:]

    res0 = 0
    p = 0
    for j in n[::-1]:
        res0 += int(j) * (2 ** p)
        p += 1

    n += str(bin(res0 % 5))[2:]

    res = 0
    p = 0
    for j in n[::-1]:
        res += int(j) * (2 ** p)
        p += 1


    if res > 1444444416:
        b = i

print(b-a)
