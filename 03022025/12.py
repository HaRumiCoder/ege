n = '0' + (12 * '1') + (15 * '2') + (17 * '3')

while '01' in n or '02' in n or '03' in n:
    n = n.replace('01', '103', 1)
    n = n.replace('02', '10', 1)
    n = n.replace('03', '210', 1)

print(n.count('2'))