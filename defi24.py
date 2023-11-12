

# Return the lexicograph permutation oreder of 
# a list of number.

def factorielleGeneration(number) :
    for singleNumber in number :
            
    pass


values = []
baseNumbers = "0123456789"
values.append(baseNumbers)
currentNumber = ""
for i in range(1, 10) :
    currentNumber += baseNumbers[i] + baseNumbers[0:i] + baseNumbers[i+1:] 
    values.append(currentNumber)
    currentNumber = ""

for number in value :


print(values)
