from math import sqrt

#todo go back and make these all "bullet proof"

def mean(data):
    if len(data) == 0:
        print "Error: len(data) == 0, cant find mean!"
        return -1
    try:
        d = [float(i) for i in data]
        return sum(d) / len(d)
    except ValueError:
        print "Error: data from mean contains non numeric value!"
        return "N/A"

def median(data):
    if len(data) <= 1:
        if len(data) == 1:
            return data[0]
        print "Error: data set is of size 0, cant find median!"
        return -1
    s = sorted(data)
    if len(s) % 2 == 1:
        return s[len(s) / 2]
    else:
        return float(sum(s[len(s) / 2 - 1:len(s) / 2 + 1])) / 2

def adm(data):
    m = mean(sorted(data))
    a = 0.0
    for i in data:
        a += abs(float(i) - m)
    return a / len(data)

def rng(data):
    if len(data) < 2:
        print "Error: data set to small to find rng!"
        return -1
    s = sorted(data)
    return s[len(s) - 1] - s[0]

def stdDev(data):
    d = sorted(data)
    try:
        d = [float(i) for i in d]
    except ValueError:
        return -1
    m = mean(d)
    devs = [(i - m) ** 2 for i in d]
    sdxsd = sum(devs) / (len(devs) - 1)
    return sqrt(sdxsd)

def iqr(data):
    d = sorted(data)
    if len(d) >= 5:
        if len(d) % 2 == 0:
            return mean(d[len(d):]) - mean(d[:len(d)])
        else:
            return mean(d[len(d) + 1:]) - mean(d[:len(d)])
    else:
        print "ERROR: data set too small! len(data) >= 5"
        return -1
