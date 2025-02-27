P = lambda x: int(69 <= x <= 91)
Q = lambda x: int(77 <= x <= 114)

A1 = 0
A2 = 200

A = lambda x: int(A1 <= x <= A2)

def check(x):
    print(x, Q(x) <= ((P(x) == Q(x)) or (not(P(x)) <= A(x))))
    #print(f'{P(x)} <= (({Q(x)} * {not(A(x))}) <= {not(P(x))}')
    #print(f'{P(x)} <= (({Q(x) * (not(A(x)))}) <= {not(P(x))}')
    #print(f'{P(x)} <= {Q(x) * (not (A(x))) <= (not (P(x)))}')
    #print(P(x) <= ((Q(x) * (not(A(x)))) <= (not(P(x)))), '!!!!')
    return Q(x) <= ((P(x) == Q(x)) or (not(P(x)) <= A(x)))

find_A1 = True
find_A2 = True

while find_A1:
    for i in range(10, 120):
        if not check(i):
            find_A1 = False
    A1 += 1

A1 -= 2

while find_A2:
    for i in range(10, 120):
        if not check(i):
            find_A2 = False
    A2 -= 1

A2 += 2

print(A1, A2, A2 - A1)
