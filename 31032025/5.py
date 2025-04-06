def F(N):
    n = str(N)
    a = int(n[0]) + int(n[2]) + int(n[4])
    b = int(n[1]) + int(n[3])
    res = [a, b]
    res.sort()
    return int(str(res[0]) + str(res[1]))


for i in range(10000, 100000):
    if F(i) == 723:
        print(i)
        break
