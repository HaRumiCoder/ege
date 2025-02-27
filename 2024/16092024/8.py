from itertools import permutations

res = 0

li = 'ПАРАБОЛА'

sgl = 'ПРБЛ'
gl = 'АО'

def check(word):
    for i in range(7):
        if word[i] in sgl and word[i+1] in sgl:
            return False
        if word[i] in gl and word[i+1] in gl:
            return False
    return True

for i in permutations(li):
    if check(i):
        res += 1

print(res // 6) # A можно переставлять 6 способами
