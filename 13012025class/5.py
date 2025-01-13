def F(N):
    N = N * 2 + (sum(map(int, str(N)))%2)
    N = N * 2 + (sum(map(int, str(N))) % 2)
    N = N * 2 + (sum(map(int, str(N))) % 2)
    return N

a1 = 123456789//8

for i in range(a1-100, a1+100):
    if F(i) >= 123456789:
        print(i)
        break
a1 = i

a2 = 1987654321//8

for i in range(a2-50, a2+50):
    if F(i) > 1987654321:
        print(i)
        break

a2 = i - 1

print(a2-a1+1)