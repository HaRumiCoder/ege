a = '0123456789ABCDEFGH'

n = 'AB9CH'

p = 0
res = 0
for i in n[::-1]:
    res += (a.index(i) * (20 ** p))
    p += 1

print(res)