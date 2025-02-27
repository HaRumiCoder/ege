def kon(a, b):
    a2 = list(map(int, str(bin(a))[2:]))[::-1]
    b2 = list(map(int, str(bin(b))[2:]))[::-1]
    res = []
    for i in range(min([len(a2), len(b2)])):
        res.append(a2[i] * b2[i])
    return int(''.join(map(str, res[::-1])))

for A in range(200):
    work = True
    for x in range(100):
        if not( (kon(x, 25) != 0) <=  ( (kon(x, 17) == 0) <= (kon(x, A) != 0) )):
            work = False
    if work:
        print(A)
        break