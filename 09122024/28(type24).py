with open('for28') as f:
    a = f.readline()

d = {'-': '123456',
     '*': '123456',
     '1': '-*123456',
     '2': '-*123456',
     '3': '-*123456',
     '4': '-*123456',
     '5': '-*123456',
     '6': '-*123456',
     'B': '123456'}

prev = 0
res = []
length = 1
start = False

for i in a:
    if not start:
        if i == 'B':
            start = True
            prev = 'B'
            line = 'B'
        continue
    if not i in d[prev]:
        if prev == '-' or prev == '*':
            length -= 1
        res.append(length)
        length = 1
        start = False
    else:
        length += 1
        prev = i

res.append(length)
print(max(res))
