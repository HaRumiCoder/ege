alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
alphabet = alphabet[:26]
print(alphabet)

res = []
a = ''
start = False

with open('for6') as f:
    for i in f.readline():
        if i in alphabet:
            if start:
                a += i
                continue
            start = True
            a = i
        if start:
            res.append(a)
            a = ''
            start = False

print(max(res))