n = 54 * '5' + '7'

while ('722' in n) or ('557' in n):
    if '722' in n:
        n = n.replace('722', '57', 1)
    else:
        n = n.replace('557', '72', 1)

print(n)