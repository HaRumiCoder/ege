from itertools import product

def check(n):
    for i in range(11):
        if not(n[i] + n[i+1] % 2 == 0 and n[i+1] > n[i]):
            if not(n[i] + n[i+1] % 2 == 1 and n[i+1] < n[i]):
                return False
    return True

res = 0
a = range(9)
b = range(1, 9)

for i in product(b, a, a, a, a, a, a, a, a, a, a, a):
    if check(i):
        res += 1

print(res)