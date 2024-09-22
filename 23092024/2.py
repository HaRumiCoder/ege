for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (bool(x) + bool(y)) <= (bool(z) == bool(y)):
                print(x, y, z)
