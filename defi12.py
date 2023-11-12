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

value = 6
div   = 4

while div < 1000 :
    value += 1
    div = len(ensembleDiv(nbTriangulaire(value)))
    

print("value :",value,"   donne : ",div,"   ",nbTriangulaire(value))
