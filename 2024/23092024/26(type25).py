li = [''] + [str(i) for i in range(1000)]

res = []

for x in range(10):
    for y in li:
        num = '1' + str(x) + '2157' + y + '4'
        if int(num) % 2024 == 0:
            res.append([int(num), int(num) // 2024])

res.sort()
print(res)