R = []

for i in range(1, 100):
    n = str(bin(i))[2:]
    n += str(bin(i % 4))[2:]
    print(n)

    res = 0
    p = 0
    for i in n[::-1]:
        res += 2 ** p
        p += 1

    R.append(res)

result = max([len(list(filter(lambda x: a < x < a+65, R)))+1 for a in R])
print(result)

