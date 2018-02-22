
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
        elif dequ[i] == '#':
            #sqrt stuff
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
            #do numer stuff
        else:
            print "ERROR: unrecognized character " + dequ[i] + "!"
            return "unrecignized character " + dequ[i]
        




