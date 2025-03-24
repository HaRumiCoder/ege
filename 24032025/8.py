from itertools import product

glas = 'ИА'
soglas = 'ЗМ'
res = 1
for word in product('ЗИМА', repeat=5):
    if word[0] not in soglas:
        continue
    if word[-1] not in glas:
        continue
    res += 1

print(res)