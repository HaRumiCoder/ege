res = 0

for n in range(234567900, 789012345):
    a = '1' * n
    while ('111' in a):
        if '11' in a:
            a = a.replace('111', '2', 1)
        if '222' in a:
            a = a.replace('222', '11', 1)
        if '1' in a:
            a = a.replace('1', '2', 1)
    if len(a) == 3:
        res += 1

print(res)