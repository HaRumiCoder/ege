
n = list("КОМПЬТЕР")
n.sort(reverse=True)

a = len(n) ** 5

res = 0

for a1 in n:
    for a2 in n:
        for a3 in n:
            for a4 in n:
                for a5 in n:
                    res += 1
                    word = [a1, a2, a3, a4, a5]
                    if 'К' in word:
                        continue
                    if word.count('Р') == 2:
                        print(a - res + 1)





