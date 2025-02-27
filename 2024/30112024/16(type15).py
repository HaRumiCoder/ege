def kon(a, b):
    a2 = list(map(int, str(bin(a))[2:]))[::-1]
    b2 = list(map(int, str(bin(b))[2:]))[::-1]
    print(a2)
    print(b2)
    res = []
    for i in range(min([len(a2), len(b2)])):
        res.append(a2[i] * b2[i])
    print(res)
    return int(''.join(map(str, res[::-1])))

for A in range(200):
    work = True
    for x in range(100):
        if not((kon(x, 35) != 0 and  kon(x, 22) != 0) <= ((kon(x, 15) == 0) <= (kon(x, A) != 0))):
            work = False
    if work:
        print(A)
        break