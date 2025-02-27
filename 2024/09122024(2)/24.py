with open('for24') as f:
    b = f.readline()


indexA = 0
is_A = False
indexB = 0
is_B = False
length = 0
a = []

for i in range(len(b)):
    if b[i] == 'A':
        if is_A:
            a.append(length)
            i = min(indexB, indexA)
            is_A = False
            is_B = False
            length = 0
            continue
        else:
            is_A = True
            indexA = i
    if b[i] == 'B':
        if is_B:
            a.append(length)
            i = min(indexB, indexA)
            is_A = False
            is_B = False
            indexB = 0
            indexA = 0
            length = 0
            continue
        else:
            is_B = True
            indexB = i
    length += 1
print(max(a))