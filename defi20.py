

tete = [4]
iteration = 0
while tete != [] :
    iteration += 1
    if tete[len(tete)-1] > 1 :
        tete.append(tete[len(tete)-1] - 1)
        tete.append(iteration) 
    tete.pop(len(tete)-1)

print(iteration-1)
