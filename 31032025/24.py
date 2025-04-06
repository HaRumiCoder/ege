res = 0

with open('for24') as f:
    for i in f.readlines():
        if i.count('E') > i.count('A'):
            res += 1

print(res)