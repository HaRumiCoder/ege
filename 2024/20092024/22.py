import sys
sys.setrecursionlimit(10000)

def F(n):
    if n >= 30:
        return 1
    res = []
    if (30 - n) >= 2:
        res.append(F(n + 2))
    if (30 - n) >= 5:
        res.append(F(n + 5))
    res.append(F(n+1))
    return sum(res)

print(F(21))