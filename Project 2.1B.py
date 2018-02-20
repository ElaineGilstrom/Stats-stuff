import sys

sys.path.append(sys.path[0] + "/tools/")

import stats

def assignHisto(start, stop, step):
    r = []
    i = start
    while i < stop:
        t = [[i], 0]
        i += step
        t[0].append(i)
        r.append(t)
    return r

adult = assignHisto(5, 25, 2.5)
p = 0
for i in [2,2,6,10,16,4,10,1]:
    adult[p][1] = i
    p += 1

child = assignHisto(8, 24, 2)
p = 0
for i in [1,5,10,4,3,0,1,1]:
    child[p][1] = i
    p += 1

ha = []
la = []
for i in adult:
    ha += [i[0][1]] * i[1]
    la += [i[0][0]] * i[1]

hc = []
lc = []
for i in child:
    hc += [i[0][1]] * i[1]
    lc += [i[0][0]] * i[1]

print "adults mean: " + str(stats.mean(la)) + " to " + str(stats.mean(ha))
print "childs mean: " + str(stats.mean(lc)) + " to " + str(stats.mean(hc))
print "adults median: " + str(stats.median(la)) + " to " + str(stats.median(ha))
print "childs median: " + str(stats.median(lc)) + " to " + str(stats.median(hc))

