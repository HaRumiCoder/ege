P = lambda x: 10 <= x <= 29
Q = lambda x: 13 <= x <= 18

A1 = 10
A2 = 30

A = lambda x: A1 <= x <= A2

def check(x):
    return ( ( A(x) <= P(x) ) or  Q(x) )

find_A1 = True
find_A2 = True

while find_A1:
    for i in range(1, 100):
        if not check(i):
            find_A1 = False
    A1 -= 1

A1 += 2

while find_A2:
    for i in range(1, 100):
        if not check(i):
            find_A2 = False
    A2 += 1

A2 -= 2

print(A1, A2, A2 - A1 + 1)
