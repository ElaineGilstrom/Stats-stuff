import math

def gen2WayTable(data):
    t = []#[[],[]...] list of all possible value combos. No margins, no types
    k = [[],[]]# list of types. len(t) == len(k[1]), len(t[i]) == len(k[0])
    for d in data:
        if len(d) != 2:
            print "Error: data contains value of len != 2! (gen2WayTable)"
            return "Value Error"
        j = 0
        if not d[1] in k[1]:
            j = len(k)
            k[1].append(d[1])
            if len(t) > 0:
                t.append([0 for i in t[0]])
            else:
                t.append([])
        else:
            j = k[1].indexof(d[1])
        i = 0
        if not d[0] in k[0]:
            i = len(k[0])
            k[0].append(d[0])
            for z in range(0, len(t)):
                t[z].append(0)
        else:
            i = k[0].indexof(d[0])
        t[j][i] += 1
    return {"table": t, "key": k}
        
    
    
    
def weightedAvg(x, p):
    if len(x) != len(P):
        print "Error: len x != len p in weightedAvg"
        return "value error"
    try:
        sum(x)
        sum(p)
    except ValueError:
        print "Error: x or p contains non numeric type! (weightedAvg)"
        return "Value error"
    return sum([x[i] * p[i] for i in range(0,len(x))])/len(x)

def stdVariance(x,p):
    if len(x) != len(P):
        print "Error: len x != len p in stdVariance"
        return "value error"
    try:
        sum(x)
        sum(p)
    except ValueError:
        print "Error: x or p contains non numeric type! (stdVariance)"
        return "Value error"
    u = weightedAvg(x,p)
    return sum([p[i]*(x[i]-u)**2 for i in range(0,x)])
