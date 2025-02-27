a = input()
b = input()

new = ''
ost = 0
for i in range(max(len(a), len(b))):
    add = ((int(a[i]) + int(b[i])) + ost) % 5
    ost = ((int(a[i]) + int(b[i])) + ost) // 5
    new = str(add)  + new

if ost != 0:
    new = str(ost) + new
print(new)
