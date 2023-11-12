from math import sqrt

def diviseur(n) :
    if n < 2 :
        return n
    result = 1 
    for i in range(2, int(sqrt(n))+1) :
        if n%i == 0 :
            result += i + n/i
    if n == int(sqrt(n))*int(sqrt(n)) :
        result -= int(sqrt(n))
    return result 

def parfait(n) :
    return diviseur(n) == n

def deficient(n) :
    return diviseur(n) < n

def abondant(n) :
    return diviseur(n) > n

limit  = 1
result = 0
nbAbondant  = []
listeSommeAbondant = []

# La liste des nombres abondants entre 1 et 2013
# La liste des sommes de deux nombres abondants entre 1 et 2013

newLen  = 0
lastLen = 0

while limit < 2014 :
    if abondant(limit) :
        nbAbondant.append(limit)
        newLen += 1
    if newLen != lastLen : # Has a new element in the list
        for i in range(newLen) :
            checkValue = nbAbondant[i]+nbAbondant[lastLen]
            if checkValue <= 2013 and checkValue not in listeSommeAbondant :
              listeSommeAbondant.append(checkValue)
        lastLen = newLen
    limit += 1

# Ici on prend tout simplement les éléments n'étant pas dans la 
# liste des sommes d'élément abondant et le compte est bon

for i in range(1, 2014) :
    if not i in listeSommeAbondant :
        result += i

print(result)
# print(nbAbondant)
# print(set(nbAbondant)-set(liste))
