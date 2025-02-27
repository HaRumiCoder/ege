n1 = 'XYZ'
n2 = 'ABCD'
res = 0

for a1 in n1:
    for a2 in n2:
        for a3 in n2:
            for a4 in n2:
                res += 1

print(res)