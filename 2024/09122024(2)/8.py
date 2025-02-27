a = [0, 2, 3, 4, 5, 6, 7]

res = 0

for a1 in a[1:]:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    n = [a1, a2, a3, a4, a5]
                    if len(set(n)) != 5:
                        continue
                    add = True
                    for i in range(4):
                        if n[i+1] % 2 == n[i] % 2:
                            add = False
                            break
                    if add:
                        res += 1


print(res)