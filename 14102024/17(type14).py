n = (49**10) + (7**30) - 49

res = ''
while n >= 7:
    res = str(n%7) + res
    n //= 7

res = str(n) + res

print(res.count('6'))