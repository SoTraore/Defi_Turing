

def fibonacci(n) :
    f1 = 1
    f2 = 1
    fn = 0
    for i in range(3, n+1) :
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn

limit = 3
compteur = 13
while limit != 2013 :
    limit = len(str(fibonacci(compteur)))
    compteur += 1

print(compteur-1)
