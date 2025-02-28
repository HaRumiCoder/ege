from itertools import permutations

res = 0

for a in range(1, 11):
    for i in permutations('0123456789',a):
        num = ''.join(i)
        if int(num) % 5 == 0 and num[0] != '0':
            res += 1

print(res+1)

