import sys
sys.setrecursionlimit(100000)

def F(n):
    if n >= 2000:
        return 2000
    if n % 2 == 1:
        return n * F(n+1)
    return n * F(n+1) / 2

print(F(1998) /  F(2001))