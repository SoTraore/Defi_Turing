import random

# Dans ce problème THREE et NEUF sont multiple de 9
# et NINE, TROIS sont des mutliples de 3 chose que j'ai ignoré mais 
# tout de même eu la bonne solution

def alphabet(expression) :
    leters = []
    for lt in expression :
        if lt != " " and lt != "x" and lt != "=" :
            leters.append(lt)
    return set(leters)

def match_lt_num(leters, num) :
    dico = {x:y for x,y in zip(leters, num)}
    return dico

def replace(expression, dico) :
    calculate = ""
    for lt in expression :
        if lt != " " and lt != "=" and lt != "x" :
            calculate += str(dico[lt])
        else :
            calculate += lt
    return calculate.split("=")

def checkResult(left, right) :
    left  = left.strip().split(" ")
    right = right.strip().split(" ")
    calL  = int(left[0])*int(left[2])
    calR  = int(right[0])*int(right[2])
    return calL == calR

expression="THREE x NINE = TROIS x NEUF"
num = list(range(10))
leters = alphabet(expression)
dico = match_lt_num(leters, num)
expr = replace(expression, dico)

while checkResult(expr[0],expr[1]) == False :
    random.shuffle(num)
    dico = match_lt_num(leters, num)
    expr = replace(expression, dico)

print(expr[0], "   ", expr[1])
