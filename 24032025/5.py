def F(N):
    n = str(bin(N))[2:]
    if N % 2 == 0:
        n += '01'
    else:
        n += '10'
    return int(n, 2)

for i in range(100):
    a = F(i)
    if a > 102:
        print(a)
        break