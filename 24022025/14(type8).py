num = 0
res = []
for a1 in ['А', 'П', 'Р', 'С', 'У']:
    for a2 in ['А', 'П', 'Р', 'С', 'У']:
        for a3 in ['А', 'П', 'Р', 'С', 'У']:
            for a4 in ['А', 'П', 'Р', 'С', 'У']:
                for a5 in ['А', 'П', 'Р', 'С', 'У']:
                    word = a1 + a2 + a3 + a4 + a5
                    num += 1
                    if word.count('У') > 1:
                        continue
                    if 'АА' in word:
                        continue
                    res.append(num)


print(res[-1])
