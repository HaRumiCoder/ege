from itertools import permutations
s1 = 'BH BA HA HF FG FD DC GC GE CE EA'.split()
s2 = '12 14 17 24 28 35 37 38 46 58 67'
s2 += ' ' + s2[::-1]

s = {
    '12': 53,
    '14': 1,
    '17': 2,
    '24': 13,
    '28': 8,
    '35': 30,
    '46': 5,
    '58': 3,
    '67': 21}

print('1 2 3 4 5 6 7 8')
for x in permutations('ABCDEFGH'):
    if all(str(x.index(c[0]) + 1) + str(x.index(c[1]) + 1) in s2 for c in s1):
        a = list(x)
        print(*a)

print(s.get(str(a.index('B')+1) + str(a.index('H')+1)) or s.get(str(a.index('H')+1) + str(a.index('B')+1)))
print(s.get(str(a.index('A')+1) + str(a.index('E')+1)) or s.get(str(a.index('E')+1) + str(a.index('A')+1)))