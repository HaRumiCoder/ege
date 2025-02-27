res = []

li = []

with open('for17') as f:
    for i in f:
        li.append(int(i.strip()))

li = list(set(li))


for i in range(len(li)):
    for j in range(i+1, len(li)):
        if (li[i] + li[j]) % 80 != 0:
            continue
        if li[i] % 50 == 0 or li[j] % 50 == 0:
            res.append(li[i] + li[j])


print(len(res), max(res))