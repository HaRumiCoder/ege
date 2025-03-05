gr1 = []
gr2 = []
gr3 = []
with open('for27A') as f:
    for i in f.readlines():
        i = i.strip().replace(',', '.')
        a = list(map(float, i.split()))
        if a[1] < 2:
            gr1.append(a)
        elif 2 < a[1] < 6:
            gr2.append(a)
        else:
            gr3.append(a)

print(len(gr1), len(gr2), len(gr3))


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

gr3_li = []

for centre in gr3:
    sum = 0
    for i in gr3:
        sum += ( ((i[1] - centre[1])**2) + ((i[0] - centre[0])**2) )**0.5
    gr3_li.append(sum)

centreC = gr3[gr3_li.index(min(gr3_li))]

print(int((centreB[0]+centreC[0])/2*10000), int((centreC[1]+centreB[1])/2*10000))