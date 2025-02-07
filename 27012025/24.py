from operator import length_hint, truediv

with open('for24') as f:
    a = f.readline().strip()

lengths = []
leng = 0
start = False
for i in a:
    if start:
        if i == 'A':
            leng += 1
            continue
        lengths.append(leng)
        leng = 0
        start = False
        continue
    if i == 'A':
        leng = 1
        start = True

print(max(lengths   ))