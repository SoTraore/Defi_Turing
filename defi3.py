from math import sqrt

def est_premier(n) :
    if n < 2 :
        return False
    else :
        limit = int(sqrt(n))
        for i in range(2, limit+1):
            if n%i == 0 :
                return False
    return True

facteur = 20130101
diviseur = 1

for i in range(int(sqrt(facteur)), 1, -1) :
    if est_premier(i) and facteur%i == 0:
        diviseur = i
        break

for i in range(facteur//diviseur, 1, -1) :
    if est_premier(i) and facteur%i == 0 :
        print(f"The result is : {i}")
    break
