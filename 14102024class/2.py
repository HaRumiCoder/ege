n = list('ВЕРОНИКА')
n.sort()

res = 0

for a1 in n:
    for a2 in n:
        for a3 in n:
            word = [a1, a2, a3]
            if word.count('В') == 1:
                res += 1
                print(word)

                if not ('А' in [a1, a2, a3]):
                    print(res)
                    break