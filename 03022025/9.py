res = 0

with open('for9') as f:
    for i in f.readlines():
        n = list(map(int, i.strip().split('\t')))
        print(n)
        if len(set(n)) == len(n):
            continue
        if n.count(max(n)) != 1:
            continue
        summ = 0
        for j in n:
            if n.count(j) > 1:
                summ += int(j)
        if summ <= int(max(n)):
            continue
        res += 1

print(res)
