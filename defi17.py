from math import sqrt

def diviseur(n) :
    if n < 2 :
        return n
    result = 1
    for i in range(2, int(sqrt(n))+1) :
        if n%i == 0 :
            result += i + n/i
    if n == int(sqrt(n))*int(sqrt(n)) :
        result -= n
    return result

limit = 1001
result = 504

while limit < 100000 :
    value = diviseur(limit)
    if limit == diviseur(value) and limit != value:
        result += limit 
    limit += 1

print(result) 

