
def pythagore(a, b, c) :
    return a*a + b*b == c*c

liste = []

for a in range(3600) :
    for b in range(3600) :
        c = 3600 - abs(-a -b)
        if c <= 3600 :
            if pythagore(a,b,c) :
                liste.append(a*b*c)
print(max(liste))
