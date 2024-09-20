def count(N):
    res = []
    for i in range(2, int(N**0.5)):
        if N % i == 0:
            res.append(i)
            res.append(N//i)
            if len(res) > 4:
                return False
    if len(res) == 4:
        return list(sorted(res))
    return False

for i in range(210235, 210300):
    a = count(i)
    if a:
        print(a)

