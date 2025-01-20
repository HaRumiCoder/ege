a = []
start = False
prev = ''
length = 0
b = {
    'A': 'B',
    'B': 'A'
}

with open('for24') as f:
    for i in f.readline():
        if start:
            now_need = b[prev]
            if i == now_need:
                length += 1
                prev = i
            else:
                a.append(length)
                start = False
                length = 0

        elif i in 'AB':
            start = True
            prev = i
            length = 1

print(max(a))