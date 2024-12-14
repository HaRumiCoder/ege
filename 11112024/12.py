a = 125 * '8'
while ('333' in a) or ('888' in a):
    if '333' in a:
        a = a.replace('333', '8', 1)
    if '888' in a:
        a = a.replace('888', '3', 1)
print(a)