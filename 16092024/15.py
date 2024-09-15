P = lambda x: 17 <= x <= 54
Q = lambda x: 37 <= x <= 83

A1 = -100
A2 = 100

A = lambda x: A1 <= x <= A2

def check(x):
    print(x)
    #print(f'{P(x)} <= (({Q(x)} * {not(A(x))}) <= {not(P(x))}')
    #print(f'{P(x)} <= (({Q(x) * (not(A(x)))}) <= {not(P(x))}')
    #print(f'{P(x)} <= {Q(x) * (not (A(x))) <= (not (P(x)))}')
    #print(P(x) <= ((Q(x) * (not(A(x)))) <= (not(P(x)))), '!!!!')
    return P(x) <= ((Q(x) * (not(A(x)))) <= (not(P(x))))

find_A1 = True
find_A2 = True

while find_A1:
    for i in range(-100, 100):
        if not check(i):
            find_A1 = False
    A1 += 1

A1 -= 2

while find_A2:
    for i in range(-100, 100):
        if not check(i):
            find_A2 = False
    A2 -= 1

A2 += 2

print(A1, A2, A2 - A1)
