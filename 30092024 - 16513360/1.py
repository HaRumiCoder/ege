print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (bool(x) <= (bool(y) == bool(w)) ) * (bool(y) == (bool(w) <= bool(z)) ):
                    print(x, y, z, w)
