li = ['А', 'В', 'Л', 'О', 'Р']

stop = False
res = 0
for a1 in li:
    for a2 in li:
        for a3 in li:
            for a4 in li:
                res += 1
                if a1 == 'Л':
                    stop = True
                    print(res)
                    break
            if stop:
                break
        if stop:
            break
    if stop:
        break

print(res)