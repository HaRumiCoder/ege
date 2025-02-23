def f(n):
    N = str(n)
    a = [int(N[0]) + int(N[1]), int(N[1]) + int(N[2])]
    a.sort()
    a = list(map(str, a))
    return ''.join(a)

res = 0

for i in range(100, 1000):
    if f(i) == '1216':
        res += 1

print(res)