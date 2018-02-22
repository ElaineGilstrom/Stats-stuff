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
    if !isinstance(data, dict):
        print "ERROR: Var not dictionary"
        return False
    for i in data.keys():
        if !isinstance(i, str):
            print "ERROR: Var contians non-string key"
            return False
        elif len(i) != 1:
            print "ERROR: Var contains key that is not len(1)!"
            return False
        try:
            float(data[i])
        except ValueError:
            print "ERROR: Vars contains non-numeric
            return False
    return True

def nAsStr(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def solve(var, equ):
    if !checkVarFormat(var):
        print "ERROR: bad var format in solve"
        return "bad var format"
    dequ = equ.remove(" ")
    regx = "#^*/+-"# #=square root, ^=exponent
    i = 0
    while !nAsStr(dequ):
        if dequ[i] == "(":
            j = i
            pers = 0
            while dequ[j] != or pers > 0:
                if dequ[j] == "(":
                    pers += 1
                elif dequ[j] == ")":
                    pers -= 1
                j += 1
            if j <= i + 1:
                print "ERROR: invalid syntax '()' in equ. in solve"
                return "syntax error"
            dequ = dequ.replace(dequ[i: j + 1], str(solve(var, dequ[i + 1: j])))
        #todo finish writting code for sqrt, exp, multi, div, add, sub
        
    
def SSE(dp, var, equ):
    if !checkDPFormat(dp):
        print "ERROR: invalid dotplot (dp) format in SSE"
        return -1
    if !checkVarFormat(var):
        print "ERROR: invalid var format in SSE"
        return -2
    if 'x' not in equ:
        print "ERROR: must have x in equ. in SSE"
        return -3
    r = 0
    for i in dp:
        var["x"] = i[0]
        r += (i[1] - solve(var, equ)) ** 2
    return r

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
    
def findLSRline(dp):
    if !checkDPFormat(dp):
        print "ERROR: invalid dotplot format in findLSRline"
        return "invalid dotplot format"
    r = CorrCoef(dp)
    x = [i[0] for i in dp]
    sx = stats.stdDev(x)
    y = [i[1] for i in dp]
    sy = stats.stdDev(y)
    b = (r * sy) / sx
    a = stats.mean(y) - b * stats.mean(x)
    #todo figure out a format to return this as
    
    
