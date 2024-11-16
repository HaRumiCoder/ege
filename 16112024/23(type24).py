with open('for23') as f:
    line = f.readline()

max_len = 0

a = []

for i in range(len(line)):
    length = 2
    counter = 0
    prev = False
    while counter <= 140 and i + length < len(line):
        if prev and line[i+length-1] == 'D':
            counter += 1
            prev = False
        else:
            if line[i+length-1] == 'C':
                prev = True
    a.append(length)

print(max(a))