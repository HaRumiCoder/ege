def fu(a,b,m):
    if a + b>=49:
        return m % 2==0
    if m==0:
        return 0
    h=[fu(a+1,b,m-1),fu(a*3,b,m-1),fu(a,b+1,m-1),fu(a,b*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

def fu2(a,b,m):
    if a + b>=49:
        return m % 2==0
    if m==0:
        return 0
    h=[fu2(a+1,b,m-1),fu2(a*3,b,m-1),fu2(a,b+1,m-1),fu2(a,b*3,m-1)]
    return any(h)

print(19, [s for s in range(1, 44) if fu2(5,s,2)])
print(20, [s for s in range(1, 44) if not fu(5,s,1) and fu(5,s,3)])
print(21, [s for s in range(1, 44) if not fu(5,s,2) and fu(5,s,4)])