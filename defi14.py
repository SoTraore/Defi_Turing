

def syracus(n) :
    liste = [n]
    while n > 1 :
        if n%2 == 0 :
            n = n//2
        else :
            n = 3*n+1
        liste.append(n)
    return len(liste)

depart = 1499999
maxi = syracus(depart) 
mini = depart

while  depart > 1 :
    nouv = syracus(depart) 
    if nouv >= maxi :
        maxi = nouv
        if depart < mini :
            mini = depart
    depart -= 1

print(maxi,"    ", mini)

