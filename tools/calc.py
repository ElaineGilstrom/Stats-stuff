import math

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

def solve(var, equ):
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
                    #TODO: parse num, sqrt it
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


