res = 0

with open('for10') as f:
    for i in f.readlines():
        i = i.strip().split('\t')
        if len(set(i)) != 5:
            continue
        chet = []
        nechet = []
        print(i, chet, nechet)
        for a in i:
            if int(a) % 2 == 0:
                chet.append(int(a))
            else:
                nechet.append(int(a))
        if len(chet) <= len(nechet):
            continue
        if sum(chet) < sum(nechet):
            res += 1

print(res)

