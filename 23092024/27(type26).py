from math import ceil

a = []

with open('for27') as f:
    f.readline()
    for i in f.readlines():
        a.append(int(i.strip()))

a.sort()

discount = list(filter(lambda x: x>100, a))
without_d = list(filter(lambda x: x<=100, a))

d1 = discount[:len(discount)//2]
d2 = discount[len(discount)//2:]

print(ceil(0.7 * sum(d1)) + sum(d2) + sum(without_d), d1[-1])