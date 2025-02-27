P = lambda x: 22 <= x <= 72
Q = lambda x: 42 <= x <= 102

A1 = 22
A2 = 102

A = lambda x: A1 <= x <= A2

def check(x):
    return not( not(A(x)) * (P(x)) ) + Q(x)

find_A1 = True
find_A2 = True

while find_A1:
    for i in range(22, 102):
        if check(i):
            find_A1 = False
    A1 += 1

A1 -= 2

while find_A2:
    for i in range(22, 102  ):
        if check(i):
            find_A2 = False
    A2 -= 1

A2 += 2

print(A1, A2, A2 - A1)

#Не понимаю, что не так