import sys
sys.setrecursionlimit(100000)

def F(n):
    if n < 10:
        return n
    return F(n%10) + F(n//10)

print(F(1000000))