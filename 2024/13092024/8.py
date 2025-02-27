li = ['А', 'В', 'О', 'Р', 'Т']

stop = False
res = 0
for a1 in li:
    for a2 in li:
        for a3 in li:
            for a4 in li:
                res += 1
                if a1 + a2 + a3 + a4 == 'ТАРА':
                    stop = True
                    break
                print(a1 + a2 + a3 + a4, res)
            if stop:
                break
        if stop:
            break
    if stop:
        break

print(res)