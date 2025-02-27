shops = {}
f = open('for3')

for i in f:
    a = i.strip().split('\t')
    shops[a[0][2:]] = (shops.get(a[0][2:]) or 0) + int(a[1])

print(shops)

print(max(shops.items(), key = lambda x: x[1]))
