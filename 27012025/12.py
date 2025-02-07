n = 99 * '1'

while '111' in n:
    if '222' in n:
        n = n.replace('222', '1', 1)
    else:
        n = n.replace('111', '2', 1)

print(n)