with open('for24') as f:
    a = f.readline()

res = []
start = False
length = 0

for i in a:
    if i == 'B':
        if start:
            length += 1
        else:
            start = True
            length = 1
    else:
        if length != 0:
            res.append(length)
        length = 0
        start = False

print(max(res))
