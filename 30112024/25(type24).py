with open('for25') as f:
    a = f.readline()

d = {'Q': '124',
     'R': '124',
     'W': '124',
     '1': 'QRW',
     '2': 'QRW',
     '4': 'QRW'}

prev = a[0]
res = []
length = 1

for i in a[1:]:
    if i not in d[prev]:
        res.append(length)
        length = 1
    else:
        length += 1
    prev = i

print(max(res))
