def F(N):
    n = str(bin(N))[2:]
    n = n + str(sum(list(map(int, n)))%2)
    n = n + str(sum(list(map(int, n))) % 2)

    return int(n, 2)

for i in range(100):
    if F(i) > 93:
        print(F(i))
        break