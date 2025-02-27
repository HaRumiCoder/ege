from itertools import permutations
m = 0
n = 0
a = [m, 0, 1]
b = [1, 0, 1]
c = [1, 0, 0]
d = [1, n, 0]

li = [a, b, c, d]

def check(x, y, z, w):
    return (bool(x) + bool(y)) <= (bool(z) * bool(w)) == ((bool(x) * bool(z)) <= (bool(w) + bool(y)))

for m, n in list(permutations([1, 1, 0, 0], 2)):
    for x, y, z, w in list(permutations(li)):
        checked = False
        for i in range(3):
            if check(x[i], y[i], z[i], w[i]):
                checked = True
            else:
                checked = False
        if checked:
            print(x, y, z, w)


