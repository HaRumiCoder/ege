f = open("for24").readline()

maxx = 0
res = 0

for i in range(len(f)-1):
    if set([f[i]] + [f[i+1]]) != {'a', 'd'}:
        res += 1
    else:
        if res > maxx:
            maxx = res
        res = 0

print(maxx)
