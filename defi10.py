from math import sqrt

def premier(n) :
    if n < 2 :
        return False
    for index in range(2, int(sqrt(n))+1) :
        if n%index == 0 :
            return False
    return True

def liste_premier(n, L=[2]) :
    if n < 2 :
        return False
    for num in L :
        if n%num == 0 :
            return False
        if num > int(sqrt(n))+1 :
            L.append(n)
            return True
    L.append(n)
    return True

continu = True
index = 2
somme = 2
primary = [2]

while index < 10000000:
    if liste_premier(index, primary) :
        somme += index
    index += 1

print(sum(set(primary)))
