def F(n):
    if n < 15:
        return n
    return F(n%15) * F(n//15)

res = 0


for i in range(1000000):
    if i % 15 == 0:
        continue
    a = F(i)
    print(a)
    if a >7560:
        print(i)
        break
