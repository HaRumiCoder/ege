for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((bool(x) + (not bool(y))) * ((not bool(z)) == bool(w))) <= (bool(y) * bool(z))):
                    print(x, y, z, w)
