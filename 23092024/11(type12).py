N = '1' * 82

while '11111' in N or '888' in N:
    if '11111' in N:
        N = N.replace('11111', '888', 1)
    else:
        N = N.replace('888', '8', 1)

print(N)