res = 0

chet = '02468'

def check(N):
    for i in N:
        if i in chet:
            return False
    return True


for i in range(1000, 10000):
    N = str(i)
    if not check(N):
        continue
    li = list(sorted([int(N[0])+int(N[1]), int(N[2])+int(N[3])]))
    if ''.join(map(str, li)) == '616':
        print(i)
        res += 1

print(res)
