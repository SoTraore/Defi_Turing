import random

def aleatoire() :
    liste = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(liste)
    return "".join(liste)

def checkValue(string) :
    k = 1
    limit = len(string)
    value = 0
    while k < limit :
        value = int(string[0:k])
        if value%k != 0 and value != 0 :
            return False
        k += 1
    return True

randValue = '123456789'

while not checkValue(randValue) :
    randValue = str(aleatoire())

print(randValue)
