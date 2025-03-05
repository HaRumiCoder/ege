def f(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i + (n // i)
    return 0

res = []

for i in range(800_000, 1_000_000):
    m = f(i)
    if m % 10 == 4:
        res.append([i, m])
        if len(res) == 5:
            break

print(res)