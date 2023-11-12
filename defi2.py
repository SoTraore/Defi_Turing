

result = 0
f1 = 1
f2 = 1
sum_impair = 2 
while result < 4000000 :
    if result%2 != 0 :
        sum_impair += result
    result = f1 + f2
    f1 = f2
    f2 = result
print(sum_impair)
