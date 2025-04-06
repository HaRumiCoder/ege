A = (2 * (216 ** 6)) + (3 * (36 ** 9)) - 432

res = []
while A >= 6:
    res.append(A%6)
    A //= 6

res.append(A)

print(res.count(5))