

def reverse(word) :  
    rev = ""
    for index in range((len(word)-1), -1, -1) :
        rev += word[index]
    return rev

value = 10000000
back  = True
while back :
    check = value*4
    if check == int(reverse(str(value))) :
        back = False
        value += 1
    value -= 1

print(value)
