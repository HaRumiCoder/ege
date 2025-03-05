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
users = dict(filter(lambda x: x[1][0] > 0, users.items()))
li = list(users.items())
prohod = li[:len(li)//4][-1][1]


print(list(dict(filter(lambda x: x[1] < prohod, users.items())).items())[0])

second_chance = dict(filter(lambda x: x[1] < prohod, users.items()))
li2 = list(second_chance.items())
prohod2 = li2[:len(li2)//10][-1][1]
print(second_chance)
print(len(dict(filter(lambda x: x[1] >= prohod2, second_chance.items()))))