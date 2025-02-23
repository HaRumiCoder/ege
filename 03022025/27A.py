gr1 = []
gr2 = []

with open('for27A') as f:
    for i in f.readlines():
        i = i.strip().replace(',', '.')
        a = list(map(float, i.split()))
        if a[0] < 1:
            gr1.append(a)
        else:
            gr2.append(a)

gr1_li = []

for centre in gr1:
    sum = 0
    for i in gr1:
        sum += ( ((i[1] - centre[1])**2) + ((i[0] - centre[0])**2) )**0.5
    gr1_li.append(sum)

centreA = gr1[gr1_li.index(min(gr1_li))]

gr2_li = []

for centre in gr2:
    sum = 0
    for i in gr2:
        sum += ( ((i[1] - centre[1])**2) + ((i[0] - centre[0])**2) )**0.5
    gr2_li.append(sum)

centreB = gr2[gr2_li.index(min(gr2_li))]

print(int((centreA[0]+centreB[0])/2*10000), int((centreA[1]+centreB[1])/2*10000))