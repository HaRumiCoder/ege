res = []

for a1 in [''] + list(range(10)):
    for a2 in [''] + list(range(10)):
        for b in range(10):
            for c in range(10):
                num = '1' + str(b) + '4' + str(a1) + str(a2) + '6' + str(c) + '8'
                if int(num) % 2622 == 0:
                    res.append([int(num),int(num) // 2622])

res.sort()
print(res)

