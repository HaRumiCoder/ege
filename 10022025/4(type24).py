with open('for4') as f:
    a = f.readline()

symbols = {'-': '6789',
           '*': '6789',
           '0': '06789-*',
           '6': '06789-*',
           '7': '06789-*',
           '8': '06789-*',
           '9': '06789-*'}



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
    if a[i] in symbols[prev]:
        prev = a[i]
        b += a[i]
        continue
    if prev in ['-', '*']:
        if a[i] == 0 and a[i+1] in ['-', '*']:
            b += a[i]
            prev = '0'
            continue
    start = False
    res.append(b[:-1])
    b = ''
    if a[i] not in '0*-':
        start = True
        prev = a[i]
        b = prev

print(len(list(sorted(res, key=lambda x: len(x)))[-1]))