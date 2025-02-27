print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (bool(y) <= bool(z)) * (not ((bool(y) + bool(w)) <= (bool(z) * bool(x)))):
                    print(x, y, z, w)
