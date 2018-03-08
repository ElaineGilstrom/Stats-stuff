import math

def checkVarFormat(data):
    if not isinstance(data, dict):
        print "ERROR: Var not dictionary"
        return False
    for i in data.keys():
        if not isinstance(i, str):
            print "ERROR: Var contians non-string key"
            return False
        elif len(i) != 1:
            print "ERROR: Var contains key that is not len(1)!"
            return False
        try:
            float(data[i])
        except ValueError:
            print "ERROR: Vars contains non-numeric"
            return False
    return True

def solveV2(var, equ):
    if not checkVarFormat(var):
        print "ERROR: bad var format in solve"
        return "bad var format"
    dequ = equ.remove(" ")
    i = 0
    #loop 1 for parenthesies
    while i < len(dequ):
        if dequ[i] != "(":
            i += 1
            continue
        p = getPers(dequ, i)
        pe = i + len(p) + 2#pe == index of ending ) for this set of pers + 1
        fm = 1.0
        am = 1.0
        if i != 0:
            j = i - 1
            if dequ[j].isnumeric():
                while j >= 0 and dequ[j].isnumeric():
                    j -= 1
                j += 1
                fm = float(dequ[j:i])
            elif dequ[j].isalpha():
                fm = var[dequ[j]]
        if pe < len(dequ):
            if dequ[pe].isalpha():
                am = var[dequ[pe]]
                pe += 1
            elif dequ[pe].isnumeric():
                x = pe
                while x < len(dequ) and dequ[x].isnumeric():
                    x += 1
                am = float(dequ[pe: x])
                pe = x
                
        dequ = dequ[:j] + str(fm * solveV2(p) * am) + dequ[pe:]
    #loop 2 for exp/roots
    i = 0
    while i < len(dequ):
        if dequ[i] == "^":
            if i == 0 or i > len(dequ) - 2:
                print "ERROR: no num/var " + ("before" if i == 0 else "after") + " ^ in solve!"
                return "syntax error"
            b = 1
            if dequ[i - 1].isalpha():
                b = var[dequ[i - 1]]
            elif isNum(dequ[i - 1]) or dequ[i - 1] == ".":
                b = grabNumB(dequ)
            else:
                print "ERROR: " + dequ[i - 1] + "cannot precede ^ in solve"
                return "syntax error"

            e = 1
            if dequ[i + 1].isalpha():
                e = var[dequ[i + 1]]
            elif isNum(dequ[i + 1]) or dequ[i + 1] == ".":
                e = grabNumF(dequ, i)
            else:
                print "ERROR: " + dequ[i + 1] + " cannot follow ^ in solve!"
                return "syntax error"
        elif dequ[i] == "#":
            
        else:
            i += 1
            continue
    try:
        return float(dequ)
    except ValueError:
        print "Errrrr: I fucked up and missed something."
        print "dequ is not numeric"
        return dequ

def grabNumB(s, i):
    j = i - 2
    while j >= 0 and isNum(s[j:i]):
        j -= 1
    j += 1
    return float(s[j:i])

def grabNuMF(s, i):
    j = i + 1
    while j < len(s) and isNum(s[i + 1: j]):
        j += 1
    j -= 1
    if j == len(s) - 1:
        if isNum(s[i + 1:]):
            return float(s[i + 1:])
    return float(s[i + 1:j])

def isNum(s):
    try:
        n = float(s)
        return True
    except ValueError:
        return False

def solve(var, equ):#TODO: modify for better order of ops
    if !checkVarFormat(var):
        print "ERROR: bad var format in solve"
        return "bad var format"
    dequ = equ.remove(" ")
    regx = "#^*/+-"# #=square root, ^=exponent
    i = 0
    while !nAsStr(dequ):
        if dequ[i] == "(":
            p = getPers(dequ, i)
            if isinstance(p, int):
                if p == 0:
                    return "programmer error"
                if p == 1 or p == 2:
                    return "syntax error"
            dequ = dequ.replace(dequ[i: j + 1], str(solve(var, p)))
        #todo finish writting code for sqrt, exp, multi, div, add, sub
        elif dequ[i] == '#':
            #sqrt stuff
            i += 1
            if i < len(dequ):
                if dequ[i] == "(":
                    dequ = dequ.replace(dequ[i: j + 1], str(solve(var, p)))
                elif dequ[i].isalpha():
                    dequ = dequ[:i - 1] + math.sqrt(var[dequ[i]]) + dequ[i + 1:]
                elif dequ[i].isnumeric():
                    j = i
                    while j < len(dequ) and dequ[j].isnumeric():
                        j += 1
                    dequ = dequ[:i - 1] + math.sqrt(float(dequ[i:j])) + dequ[j:]
            else:
                print "ERROR: sqrt at end of equ in solve"
                return "syntax error"
        elif dequ[i] == "^":
            #exponent stuff
        elif dequ[i] == "/":
            #division stuff
        elif dequ[i] == "*":
            #multi stuff
        elif dequ[i] == "-":
            #sub stuff
        elif dequ[i] == "+":
            #add stuff
        elif dequ[i].isalpha():
            #do variable stuff
        elif dequ[i].isdigit():
            i += 1
            continue
        else:
            print "ERROR: unrecognized character " + dequ[i] + "!"
            return "unrecignized character " + dequ[i]
        
def getPers(s, start):
    if start >= len(s):
        print "ERROR: start >= len(s) in getPers!"
        return 0
    j = start 
    pers = 0
    while (s[j] != ")" or pers > 0) and j < len(s):
        if s[j] == "(":
            pers += 1
        elif s[j] == ")":
            pers -= 1
        j += 1
    if j >= len(s):
        print "ERROR: invalid syntax no closing ')' present! in getPers"
        return 2
    if j <= start + 1:
        print "ERROR: invalid syntax '()' in s. in getPers"
        return 1
    return s[start + 1:j]



