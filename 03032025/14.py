n = (36**7)+(6**19)-18
res = ''
while n >= 6:
    res += str(n % 6)
    n = n // 6

res += str(n)

print(res.count('0'))