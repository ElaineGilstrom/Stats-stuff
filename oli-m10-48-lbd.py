import sys

sys.path.append(sys.path[0] + "/tools/")

import stats
import parsers

data = parsers.parseCSV(sys.path[0] + "/dataSets/sdintuition.csv")

info = data.pop(0)

for i in range(0,len(info)):
    print info[i] + ": " + str(stats.stdDev([j[i] for j in data]))
