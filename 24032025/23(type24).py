info = {}

with open('for23') as f:
    a = f.readline()

prev = False

for i in a:
    if prev:
        info[i] = (info.get(i) or 0) + 1
    if i == 'E':
        prev = True
    else:
        prev = False

info = dict(sorted(info.items(), key=lambda x: x[1]))

print(info)