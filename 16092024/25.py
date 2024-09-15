li = ['', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

res = []

for a1 in li:
    for a2 in li:
        for a3 in li:
            for i in range(9):
                num = int('1' + str(a1) + str(a2) + str(a3) + '4302' + str(i) + '1')
                if num % 3147 == 0:
                    res.append(num)

res = list(set(res))
print(res)