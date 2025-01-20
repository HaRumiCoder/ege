print('0' + str(bin(84))[2:])
print(11110000)
print('0' + str(bin(80))[2:])

res = 0
p = 0

for i in '11110000'[::-1]:
    res += int(i) * (2 ** p)
    p += 1

print(res)