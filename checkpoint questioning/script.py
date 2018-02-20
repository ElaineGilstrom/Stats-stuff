
def median(s):
    if len(s) % 2 == 1:
        return s[len(s) / 2]
    else:
        return float(sum(s[len(s) / 2 - 1:len(s) / 2 + 1])) / 2

def mean(data):
    return sum(data) / len(data)

histo = [
    [[48,56],7],
    [[56,64],7],
    [[64,72],10],
    [[72,80],8],
    [[80,88],12],
    [[88,96],17],
    [[96,104],9]
    ]

mini = []
maxi = []

for i in histo:
    for j in range(0,i[1]):
        mini.append(i[0][0])
        maxi.append(i[0][1])

print "Min mean: " + str(mean(mini))
print "Max mean: " + str(mean(maxi))
print
print "Min median: " + str(median(mini))
print "Max median: " + str(median(maxi))
