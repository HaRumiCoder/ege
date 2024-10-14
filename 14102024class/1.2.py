from itertools import product

s = sorted('КЛРТ')
li = [0] + list(product(s, repeat=4))
print(li[67])