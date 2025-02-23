res = []

for a in range(10):
    for b1 in [''] + list(range(10)):
        for b2 in [''] + list(range(10)):
            for b3 in [''] + list(range(10)):
                num = int('3' + str(a) + '6906' + str(b1) + str(b2) + str(b3) + '4')
                if num % 2024 == 0:
                    res.append(num)

res.sort()

print(res)

