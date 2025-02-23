users = {}

with open('for26') as f:
    for i in range(int(f.readline().strip())):
        info = list(map(int, f.readline().strip().split()))
        id_user = info.pop(0)
        summ = sum(info)
        plus = sum(list(filter(lambda x: x>0, info)))
        ans = 10 - info.count(0)
        users[id_user] = [summ, plus, ans]


users = dict(sorted(users.items(), key=lambda x: (x[1], -x[0]), reverse=True))

li = list(users.items())

prohod = li[:len(li)//3][-1][1]

print(dict(filter(lambda x: x[1] >= prohod, users.items())))

print(li[len(dict(filter(lambda x: x[1] >= prohod, users.items())))])
print(li[1500-1])

place1500 = li[1500-1][1]
print(len(dict(filter(lambda x: x[1] == place1500, users.items()))))