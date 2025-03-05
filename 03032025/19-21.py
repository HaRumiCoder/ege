def fu(a,m):
    if a<=17  : return m%2==0
    if m==0:return 0
    h=[fu(a-5, m-1)]
    if a % 2 == 0:
        h.append(fu(a//2))
    if
    return any(h) if (m-1)%2==0 else all(h)



print(19,[s for s in range(1, 37) if fu(s,2)])
print(20,[s for s in range(1, 37) if not fu(s,1) and fu(s,3)])
print(21,[s for s in range(1, 37) if not fu(s,2) and fu(s,4)])

