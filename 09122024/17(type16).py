import sys
sys.setrecursionlimit(100000)

def F(n):
    if n < 11:
        return 10
    return n + F(n-1)

print(F(2024) -  F(2022))