n = 125 + (25**3) + (5**9)

res = ''
while n >= 5:
    res = str(n%5) + res
    n //= 5

res = str(n) + res

print(res.count('0'))