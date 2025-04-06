candidate = []

for i in range(1, 10**5):
    if i ** 2 >= 123456789 and i ** 2 <= 223456789:
        candidate.append(i)


def check(n):
    res = []
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    res.append(int(n**0.5))
    if len(res) == 3:
        return max(res)
    return 0



for i in candidate:
    k = check(i**2)
    if k:
        print(i**2, k)

