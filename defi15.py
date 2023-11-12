import random

# liste = range(1, 10)
# Non utilisé donc ne serre pas trop 
# Mais la façon de résolution de ce problème est remarquable
def generate(liste):
    random.shuffle(liste)
    return liste 


def calculate(liste) :
    rows = 1
    totalR = 0
    totalC = 0
    c1 = 1
    c2 = 1
    c3 = 1
    for i in range(0, 3):
        rows = 1
        for j in range(0, 3) :
            index = i+j*3
            rows *= liste[index]
            if j == 0 :
                c1 *= liste[index]
            if j == 1 :
                c2 *= liste[index]
            if j == 2 :
                c3 *= liste[index]
        totalR += rows
    totalC += c1 + c2 + c3
    return totalR + totalC

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
maxi = calculate(liste)
mini = maxi
limit = 362880

while limit > 0 :
    # generate aleatory liste of 3x3
    # and put the result in liste variable
    random.shuffle(liste)
    value = calculate(liste)
    if value > maxi :
        maxi = value
    else :
        if value < mini :
            mini = value
    limit -= 1

print(maxi*mini)
