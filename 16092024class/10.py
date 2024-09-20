N = 127 * '9'

while ('333' in N) or ('999' in N):
    if '333' in N:
        N = N.replace('333', '9', 1)
    else:
        N = N.replace('999', '3', 1)

print(N)