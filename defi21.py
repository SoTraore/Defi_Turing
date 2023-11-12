

def checkValue(n) :
    for i in range(0, len(n)) :
        ch  = n[i]
        if ch in n[0:i] or ch in n[i+1:len(n)] :
            return False
    return True

result = 10
maxi = 26
afterValue = 0
beforValue = 0
check = False

for i in range(10, 2012) :
    if checkValue(str(i)) :
        if not check :
            check = True
            beforValue = i
        else :
            check = False
            afterValue = i
        newValue = abs(beforValue - afterValue)
        if newValue > maxi :
            maxi = newValue
        result += 1

print("The year : ",result," the maxValue : ", maxi,"result*maxi = ",result*maxi)
