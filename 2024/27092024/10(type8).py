a = ['А', 'К', 'Р', 'У']

i = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                        i += 1
                        if i == 450:
                            print(a1, a2, a3, a4, a5, sep='')