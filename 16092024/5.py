b = 0

for i in range(1, 100):
    n = list(map(int, str(bin(i))[2:]))
    for j in range(2):
        n.append(sum(n) % 2)
    p = 0
    res = 0
    for a in n[::-1]:
        res += a * (2 ** p)
        p += 1
    if res >= 100:
        print(b)
        break
    b = int(res)

