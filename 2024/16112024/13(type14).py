minn = 1000000000000000
res = 0
for x in range(0, 8):
    for y  in range(1, 8):
        a = [y, 0, 4, x, 5]
        res_a = 0
        p = 0
        for i in a[::-1]:
            res_a += i * (11**p)
            p += 1

        b = [2, 5, 3, x, y]
        res_b = 0
        p = 0
        for i in b[::-1]:
            res_b += i * (8 ** p)
            p += 1


        print((res_a + res_b) % 117, x, y)
        if (res_a + res_b) % 117 == 0 and (res_a + res_b) < minn:
            minn = (res_a + res_b)
            res = (res_a + res_b) // 117

print(res)