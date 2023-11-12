
def sameNumber(m, n) :
    if len(str(m)) != len(str(n)) :
        return False
    # Declaration of some variable 
    d1 = {x:0 for x in str(m)}
    d2 = {x:0 for x in str(n)}
    it = iter(str(n))
    # Check if they same numbers
    for lt1 in str(m) :
        lt2 = next(it)
        d1[lt1] += 1
        d2[lt2] += 1
        if lt1 not in str(n) :
            return False
        if lt2 not in str(m) :
            return False
    # Check if they same number of each single number
    for key,_ in d1.items() :
        if d1[key] != d2[key] :
            return False
    return True

liste = []

for index in range(100000, 1000000) :
    if len(str(index * 8)) > 8 : 
        break
    else :
        if sameNumber(index, index*8) :
            print("--> : ",index)
            liste.append(index)

print("The result is : ",sum(liste))
