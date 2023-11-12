
Hbleu = [2]
HVert = [2]

Xo = 2
Yo = 2
Une_Deux = True

for i in range(2, 2014) :
    if Une_Deux :
        Xo += 10
        Yo += 12
        Une_Deux = False
    else :
        Xo += 2
        Yo += 2
        Une_Deux = True
    if Xo < 2014 :
        Hbleu.append(Xo)
    else :
        break
    if Yo < 2014 :
        HVert.append(Yo)
print(sum((set(Hbleu)).intersection(set(HVert))))
