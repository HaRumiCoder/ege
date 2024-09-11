a = '0123456789ABCDEFGHIJKLMN'

line = open('for24').readline()

length = 0
li = []

for i in line:
    if i in a:
        length += 1
    elif length:
        li.append(length)
        length = 0

print(max(li))
