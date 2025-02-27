maxx = 0

for i in range(1000):
    n = str(bin(i))[2:]
    if i % 2 == 0:
        n += '10'
    else:
        n += '01'

    res = 0
    p = 0
    for j in n[::-1]:
        res += int(j) * (2 ** p)
        p += 1

    if res > 102:
        print(maxx)
        break

    if res > maxx:
        maxx = res



