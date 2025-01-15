print('')
res = []
for a1 in range(0, 10):
    for b1 in ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        for b2 in ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            for b3 in ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num = int('3' + str(a1) + '2258' + b1 + b2 + b3 + '4')
                if num % 2024 == 0:
                    res.append(num)

res = list(set(res))
res.sort()
print(res)

