n  = (125**5 + (25**9) - 30)

res = ''
while n > 5:
    res += str(n%5)
    n //= 5

res += str(n)
print(res.count('4'))