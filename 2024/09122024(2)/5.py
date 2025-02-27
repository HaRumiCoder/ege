for i in range(1000, 10000):
    summ = []
    a = str(i)
    for j in range(3):
        summ.append(int(a[j]) + int(a[j+1]))
    summ.sort()
    if int(str(summ[1]) + str(summ[2])) == 1215:
        print(i)
        break
