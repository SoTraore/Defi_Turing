


def estPalindrome(word) :
    last = len(word)-1
    for i in range(last, last//2,-1):
        if word[i] != word[last-i] :
            return False
    return True

def pair(num) :
    return num%2 == 0

carre = 837
result = carre*carre

while not ( estPalindrome(str(result)) and pair(len(str(result))) ) :
    result = carre*carre
    carre += 1

print(carre,"   ",result)
