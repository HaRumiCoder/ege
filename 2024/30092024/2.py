print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ( (bool(y) * bool(z)) + ((bool(x) <= bool(z)) == (bool(y) <= bool(w))) ):
                    print(x, y, z, w)
