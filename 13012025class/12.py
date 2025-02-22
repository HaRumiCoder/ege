res = 0

for i in range(123_456_794, 679_901_235):
    a = i * '1'
    while '111' in a:
        if '111' in a:
            a = a.replace('111', '2', 1)
        if '222' in a:
            a = a.replace('222', '11', 1)
        if '1' in a:
            a = a.replace('1', '2', 1)
    if set(a) == {2}:
        res += 1

print(res)