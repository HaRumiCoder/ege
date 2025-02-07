res = ''

n = (25**5) + (5**14) - 5

while n >= 5:
    res = str(n % 5) + res
    n = n // 5

res = str(n) + res

print(res.count('4'))
