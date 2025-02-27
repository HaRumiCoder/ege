res = []

li = []

with open('for16') as f:
    for i in f:
        a = int(i.strip())
        li.append(a)

print(li)
min_ost = min(li) % 3
max_ost = max(li) % 7

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i] % 3 == min_ost or li[j] % 3 == min_ost:
            if li[i] % 7 == max_ost or li[j] % 7 == max_ost:
                res.append(li[i] + li[j])

print(len(res), max(res))