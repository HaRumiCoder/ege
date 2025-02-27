for i in range(10000, 999, -1):
    N = str(i)
    li = []
    for j in range(3):
        li.append(int(N[j]) + int(N[j+1]))
    li.remove(min(li))
    li.sort()
    li = map(str, li)
    if ''.join(li) == '1315':
        print(i)
        break

