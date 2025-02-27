def getM(x):
    a = 0
    b = 0
    for i in range(2, x-1):
        if x % i == 0:
            a = i
            break
    for i in range(x-1, 2, -1):
        if x % i == 0:
            b = i
            break
    return b + a


res = 0

for i in range(452022, 10000000000):
    M = getM(i)
    if M % 7 == 3:
        res += 1
        print(i, M)
    if res == 5:
        break
