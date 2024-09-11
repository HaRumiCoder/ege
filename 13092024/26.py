f = open('for26')

S, N = map(int, f.readline().strip().split())

sizes = {}
for i in f.readlines():
    sizes[int(i.strip())] = (sizes.get(int(i.strip())) or 0) + 1


sizes = dict(sorted(sizes.items()))

summ = 0
items = 0

for key, item in sizes.items():
    if key > (S - summ):
        break
    item_add = item
    add = key * item_add
    if add > (S - summ):
        item_add = (S - summ) // key
        add = item_add * key
    summ += add
    items += item_add

print(key, items, summ, S)

print(items, max(list(filter(lambda x: key + (S - summ) >= x > key,sizes.keys()))))
