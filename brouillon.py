from math import sqrt

def nbTriangulaire(n) :
    return sum(range(1,n+1))

def ensembleDiv(n) :
    limit = int(sqrt(n))+1
    liste = [1]
    for i in range(2, limit+1) :
        if n%i == 0 :
            liste.append(i)
            liste.append(n/i)
    return list(set(liste))

def diviseur(n, p=2) :
    if n <= 1 :
        return n
    if n%p == 0 :
        return diviseur(n//p, p)+1
    else :
        p += 1
        return diviseur(n,p)

def recursif(n,p=2) :
    if n < 2 :
        return n
    else :
        p = int(sqrt(n))+1
    if n%p == 0 :
        return recursif(p)+1
    else :
        return recursif(n,p+1)

def nbDiviseur(n) :
    nbDiv = 2
    for i in range(2, int(sqrt(n))+1) :
        if n%i == 0 :
            nbDiv += 1
    return nbDiv

def nbDiv(n) :
    if n < 2 :
        return n
    div = int(sqrt(n))+1
    result = 0
    while div > 1 :
        if n%div == 0 :
            result += 1 + nbDiv(div)
        div -= 1
    return result

def arbreDiv(n) :
    if n < 2 :
        return n
    liste = [n,1]
    p = 2
    while n > 1 :
        if n%p == 0 :
            liste.append(n/p)
            liste.append(p)
            n = n/p
            p = 2
        elif p > int(sqrt(n)) :
            liste.append(n)
            break
        else :
            p += 1
    return len(liste)

value = 6
div   = 4

while div < 1000 :
    value += 1
    div = len(ensembleDiv(nbTriangulaire(value)))
    

print("value :",value,"   donne : ",div,"   ",nbTriangulaire(value))
