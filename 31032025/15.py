A1 = -9
A2 = 6

A = lambda x: A1 <= x <= A2

def check(x, y):
    return (A(x) <= (x**2 <= 81)) and ((y**2 <= 36) <= A(y))

find_A1 = True
find_A2 = True



while find_A2:
    for x in range(1, 100):
        for y in range(1, 100):
            if not check(x, y):
                find_A2 = False
    A2 += 1

A2 -= 2

print(A1, A2, A2 - A1)
