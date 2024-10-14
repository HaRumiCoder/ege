
n = list("МАНГУСТ")
n.sort(reverse=True)

a = len(n) ** 6

res = 0

for a1 in n:
    for a2 in n:
        for a3 in n:
            for a4 in n:
                for a5 in n:
                    for a6 in n:
                        res += 1
                        word = [a1, a2, a3, a4, a5, a6]
                        if a1 == 'У':
                            continue
                        if word.count('М') != 2:
                            continue
                        if word.count('Г') <= 1:
                            print(a - res + 1)





