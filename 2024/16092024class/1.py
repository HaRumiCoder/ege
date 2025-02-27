N = int(input())
new = ''
while N >= 5:
    new += (str(N%5))
    N = N // 5
new += str(N)

print(new[::-1])
