N = '7' * 85

while '333' in N or '777' in N:
    if '333' in N:
        N = N.replace('333', '7', 1)
    else:
        N = N.replace('777', '3', 1)

print(N)