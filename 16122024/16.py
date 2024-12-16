import sys
sys.setrecursionlimit(100000)

res = 0
def F(n):
    if n < 11:
        return n
    return F(n%9) + F(n//9)

for i in range(4*(6**20), 5*(6**20)):
    if F(i) == 121:
        res += 1

print(res)