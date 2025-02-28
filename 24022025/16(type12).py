n = 81 * '1'

while '00' not in n:
    n = n.replace('033', '21120', 1)
    n = n.replace('034', '22120', 1)
    n = n.replace('04', '220', 1)
    n = n.replace('030', '100', 1)

print(n)