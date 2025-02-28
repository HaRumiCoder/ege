n = 81 * '1'

while ('11111' in n) or ('888' in n):
    if '11111' in n:
        n = n.replace('11111', '88', 1)
    else:
        n = n.replace('888', '8', 1)

print(n)