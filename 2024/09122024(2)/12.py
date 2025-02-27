def is_prost(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

v = []
stop = False
for x in range(100):
    for y in range(100):
        b =  '0' + '1' * y + '2' * x
        if len(b) > 44:
            summ = x * 2 + y * 1
            while '01' in b or '02' in b:
                b = b.replace('02', '1110', 1)
                b = b.replace('01', '220', 1)

            if is_prost(sum(list(map(int, b)))):
                print(summ)
                stop = True
                break
    if stop:
        break
