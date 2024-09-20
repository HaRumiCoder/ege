N = (9**8) + (3**5) - 2

res = ''
while N >= 3:
    res = str(N%3) + res
    N //= 3

res = str(N) + res

print(res.count('2'))