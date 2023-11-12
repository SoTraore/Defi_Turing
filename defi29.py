

def isPow(n, m) :
    if n % m != 0 or m == 0 :
        return False
    if n == m :
        return True
    return isPow(n/m, m)

def isPower(n, m) :

    while n%m == 0 and n != m :
        n = n/m
    if n == m :
        return True
    return False

result = [2]

for i in range(2, 1001) :
    value = i
    # Ici c'est pour les puissances 
    if i in result :
        racine = value - 1
        while not isPower(value, racine) :
            racine -= 1
        quotien = 1
        if racine != 0 :
            quotien = racine
        quotien = value/quotien
        limit = int(1000/quotien)
        value = pow(value, limit) 
        for _ in range(limit+1, 1001) :
            value *= value
            result.append(value)
    else :
        for _ in range(2, 1001) :
            value *= value
            result.append(value)
    result = list(set(result))

        
print(len(set(result)))
