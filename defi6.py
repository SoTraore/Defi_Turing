

def facto(n) :
   result = 1
   for index in range(2, n+1):
        result *= index
   return result

result = facto(2013)
chaine = str(result)
somme = 0
for num in chaine :
    somme += int(num)
print(somme)
