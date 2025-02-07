from enum import unique

res = []

for a1 in [''] + list(range(10)):
    for a2 in [''] + list(range(10)):
        for a3 in [''] + list(range(10)):
            for b in range(10):
                n = '1' + str(a1) + str(a2) + str(a3) + '4239' + str(b) + '7'
                n = int(n)
                if n % 3147 == 0:
                    res.append(n)

res = list(set(res))
res.sort()
print(res)
