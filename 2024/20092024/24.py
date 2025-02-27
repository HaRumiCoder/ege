with open('for24') as f:
    a = f.readline()

res = 0
maxx = 0
for i in range(len(a)):
    print(a[i:i+4])
    if a[i:i+4] == 'XZZY':
        if res + 3 > maxx:
            maxx = res + 3
        res = 0
        continue
    res += 1

print(maxx)

