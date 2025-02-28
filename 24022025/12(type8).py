from itertools import *

res = []

for i in permutations('ЯРОСЛАВ', 5):
    if 'Я' in i and 'О' in i and 'А' in i:
        continue
    word = ''.join(i)
    if 'АЯ' in word or 'ЯА' in word or 'ЯО' in word or 'ОЯ' in word or 'ОА' in word or 'АО' in word or 'АА' in word or 'ОО' in word or 'ЯЯ' in word:
        continue
    res.append(word)

print(len(set(res)))