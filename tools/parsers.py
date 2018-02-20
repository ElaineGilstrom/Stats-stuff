import misc

def parseCSV(fname):
    r = []
    f = open(fname)
    for l in f:
        l = l[:len(l) - 1].split(",")
        r.append(misc.listToNums(l))
    f.close()
    return r
