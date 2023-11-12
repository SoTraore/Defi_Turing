import random
from math import sqrt

def resolve(n, a, b) :
    return n*n + a*n + b

def aleatoireCouple(liste=list(range(-1499, 1500))) :
    a = random.choice(liste)
    b = random.choice(liste)
    return a,b

def estPremier(n) :
    if n < 2 :
        return False
    limit = int(sqrt(n))
    for i in range(2, limit+1) :
        if n%i == 0 :
            return False
    return True 

maxi   = 0
limit  = 0
result = 0
while limit < 30000 :
    a, b = aleatoireCouple()
    value = 0
    liste = []
    finalResult = resolve(value, a, b)
    while estPremier(finalResult) :
        liste.append(finalResult)
        value += 1
        finalResult = resolve(value, a, b)
    value = len(set(liste))
    if value > maxi :
        maxi = value
        result = a*b
    value = 0
    liste = []
    finalResult = resolve(value, b, a)
    while estPremier(finalResult) :
        liste.append(finalResult)
        value += 1
        finalResult = resolve(value, b, a)
    value = len(set(liste))
    if value > maxi :
        maxi = value
        result = a*b
    limit += 1
    print(result)

print("La taille max : ",maxi," la valeur maxi : ",result)

