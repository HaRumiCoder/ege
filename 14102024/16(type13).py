a = str(bin(196))[2:]
b = str(bin(192))[2:]
res = ''
print(a)
print(b)
add_null = False
for i in range(len(a)):
    if add_null:
        res += '0'
        continue
    if a[i] == '0' and b[i] == '0':
        res += '1'
    if a[i] == '1' and b[i] == '0':
        res += '0'
        add_null = True
    if a[i] == '1' and b[i] == '1':
        res += '1'
    if a[i] == '0' and b[i] == '1':
        res += '1'

print(res)
