with open('for21') as f:
    a = f.readline()

f = []

for i in range(len(a)):
    if a[i] == 'F':
        f.append(i)

res = [0]

for i in range(len(f)-1):
    if a[f[i]:f[i+1]+1].count('A') <= 2:
        if res[-1] == f[i]:
            res.pop()
        else:
            res.append(f[i])
        res.append(f[i+1])

new_res = [res[i+1] - res[i] + 1 for i in range(1, len(res)-1)]

print(max(new_res))
