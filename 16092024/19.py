def F(k, turn=0, limit1=1, limit2=2):
    if turn > limit2:
        return [0]
    print(k, turn)
    if k >= 96:
        return [turn]

    var = [k+1]

    if k % 2 == 0:
        var.append(k+(k//2))
    if k % 3 == 0:
        var.append(k+(k//3))
    if k % 2 != 0 and  k % 3 != 0:
        var.append(k*2)

    print(var)

    res = []
    for j in range(len(var)):
        res.append([i for i in F(var[j], turn=turn+1)])
    return res

def check(res, turn=0):
    types = [type(i) for i in res]
    if list not in types:
        return sum(res) > 0
    can = []
    for i in res:
        can.append(check(i, turn=turn+1))
    print(res, can)
    if turn==0:
        return not(False in can)
    return True in can

a = []

for i in range(95, 0, -1):
    if check(F(i)):
        a.append(i)

print(min(a))