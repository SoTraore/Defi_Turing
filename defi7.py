from math  import sqrt
def premier(n) :
    if n < 2 :
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0 :
            return False
    return True

index = 0
compteur = 0
while compteur < 23456 :
    index += 1
    if premier(index) :
        print(index)
        compteur += 1
