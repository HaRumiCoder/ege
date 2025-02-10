def M(N):
    res = set()
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
           res |= {i, N//i}
    res = sorted(list(res))
    return res

result = []

for i in range(110_250_000,  110_300_001):
    v = M(i)
    if len(v) >= 2:
        summ = v[-2]+v[-1]
        if summ % 10_000 == 1002:
            result.append(i)

result.sort()
print(result)

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
alphabet = alphabet[:26]
print(alphabet)

