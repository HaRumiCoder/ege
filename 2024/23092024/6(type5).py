for i in range(100, 1000):
    N = str(i)
    if ''.join(list(map(str, sorted([int(N[0])+int(N[1]), int(N[1])+int(N[2])])))) == '714':
        print(i)
        break