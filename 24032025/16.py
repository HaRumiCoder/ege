import sys
sys.setrecursionlimit(1000000)

def F(n):
    if n == 0:
        return 0
    if n % 3 == 2:
        return F(n-1) + 1
    return F((n - (n % 3)) / 3)


for i in range(10000):
    if F(i) == 6:
        print(i)
        break