from math import pow

def sumPuissance(number) :
    result = 0
    for i in range(len(number)) :
        result += pow(int(number[i]), 5)
    return result

current = 11
result = 0
while True :
    if sumPuissance(str(current)) == current :
        result += current 
        print("The current value",current)
        print("The result : ",result)
    current += 1


