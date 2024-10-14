for i in range(1, 10000):
    n = str(bin(i))[2:-1]
    if i % 2 == 1:
        n += '10'
    else:
        n += '01'

    res = 0
    p = 0
    for j in n[::-1]:
        res += int(j) * (2 ** p)
        p += 1


    if res == 2018:
        print(i)
        break
