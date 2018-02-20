
def listToNums(l):
    r = []
    for i in l:
        r.append(strToNum(i))
    return r

def strToNum(s):
    r = s
    try:
        r = float(s)
    except ValueError:
        return r
    return r
