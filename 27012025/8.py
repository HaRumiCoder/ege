import string
from itertools import product

a = 0

print(string.ascii_uppercase)
for i in range(len(string.ascii_uppercase)):
    for j in product(string.ascii_uppercase, repeat=i):
        a += 1
        if j == 'FDECBA':
            print(a)