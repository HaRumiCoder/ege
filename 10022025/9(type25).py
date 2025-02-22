num = {}

def count(N):
    res = 0
    for i in range(1, N//2+1):
        if N % i == 0:
            res += 1
    return res + 1

for i in range(568_023, 569_231):
    num[i] = count(i)

num = sorted(num.items(), key=lambda x: x[1], reverse=True)
print(num)