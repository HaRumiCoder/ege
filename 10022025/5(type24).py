with open('for5') as f:
    a = f.readline()

symbols = {'-': '678',
           '*': '678',
           '0': '0678',
           '6': '0678-*',
           '7': '0678-*',
           '8': '0678-*'}



prev = a[0]
res = []
b = prev
start = True

for i in range(1, len(a)):
    if not start:
        if a[i] not in '0*-':
            prev = a[i]
            b = prev
            start = True
            continue
    if a[i] in symbols[prev]:
        prev = a[i]
        b += a[i]
        continue
    start = False
    res.append(b[:-1])
    b = ''
    if a[i] not in '0*-':
        start = True
        prev = a[i]
        b = prev

print(len(list(sorted(res, key=lambda x: len(x)))[-1]))

