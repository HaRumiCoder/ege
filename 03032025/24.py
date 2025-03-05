with open('for24') as f:
    a = f.readline().strip()

res = {}

for i in range(1, len(a)-1):
    if a[i-1] == a[i+1]:
        res[a[i]] = (res.get(a[i]) or 0) + 1

print(list(sorted(list(res.items()), key=lambda x: x[1], reverse=True))[0])