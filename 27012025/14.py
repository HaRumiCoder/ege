n = (36**8) + (6**20) - 12
res = ''
while n >= 6:
    res =  str((n % 6)) + res
    n = n // 6

res += str(n)

print(res.count('5'))