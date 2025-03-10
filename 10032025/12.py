from itertools import product, permutations


def f(n):
    while '21' in n:
        n = n.replace('21', '5', 1)
    return n

# 222111 = 555 => 222222111111 = 555555 sum = 30, + 4 '1' = 34