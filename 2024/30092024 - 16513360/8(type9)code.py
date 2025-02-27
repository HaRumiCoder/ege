res = 0
with open('for8') as f:
    for s in f:
        n = list(map(int, s.strip().split('\t')))
        s = 0
        p = 0
        k = 0
        for i in n:
            if n.count(i) == 1:
                s += i
                k += 1
            if n.count(i)==3:
                p = i
        if p != 0 and k == 3:
            if p >= (s / 3):
                res += 1
print(res)