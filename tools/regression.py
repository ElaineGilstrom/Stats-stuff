import stats

def checkDPFormat(data):
    for i in data:
        try:
            if len(i) != 2:
                return False
        except TypeError:
            return False
    return True

def checkVarFormat(data):
    for i in data:
        try:
            if len(i) != 2:
                return False
            if !isinstance(i[0], str):
                return False
            if !isinstance(i[1], int):
                return False
        except TypeError:
            return False
    return True

def solve(var, equation):#use recursion for ()
    if !checkVarFormat(var):
        print "ERROR: bad var format in solve"
        return "bad var format"
    desEqu = equation.remove(" ")
    regx = "#^*/+-"# #=square root, ^=exponent
    

def CorrCoef(data):#format: [[x,y],[x,y]..] where [x,y] represents 1 individual
    if !checkDPFormat(data):
        print "ERROR: invalid dotplot format in CorrCoef"
        return 2
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    xb = stats.mean(x)
    yb = stats.mean(y)
    if xb == "N/A" or yb == "N/A":
        print "ERROR: failed to calculate mean in CorrCoef"
        return 3
    sx = stats.stdDev(x)
    sy = stats.stdDev(y)
    if sx == -1 or sy == -1:
        print "ERROR: failed to calculate stdDev in CorrCoef"
        return 4
    s = 0
    for i in data:
        s += ((i[0] - xb) / sx) * ((i[1] - yb) / sy)
    return s / (len(data) - 1)

def SSE(dp, equation):
    if !checkDPFormat(dp):
        print "ERROR: invalid dotplot (dp) format in SSE"
        return -1
    equation = equation.remove(" ")
    
def findLSRline(dp):
    if !checkDPFormat(dp):
        print "ERROR: invalid dotplot format in findLSRline"
        return "invalid dotplot format"
    x = [i[0] for i in dp]
    y = [i[1] for i in dp]
    
    
