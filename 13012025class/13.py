from itertools import product

print(bin(172)[2:], bin(16)[2:], bin(168)[2:], bin(0)[2:])
print(bin(255)[2:], bin(255)[2:], bin(248)[2:], bin(0)[2:])

#10101100 00010000 10101*** ********
#11111111 11111111 11111000 0
#10101100    10000 10101000 0

n0 = 8
res = 0

for i in product([0,1], repeat=11):
    if (sum(i) + n0) % 5 != 0:
        res += 1

print(res)
