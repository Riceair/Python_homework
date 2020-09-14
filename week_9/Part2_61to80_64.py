number = [1,2,3]
alphabet = ['a','b','c']
print("number =",number)
print("alphabet =",alphabet)
for i in range(min(len(number),len(alphabet))):
    print(number[i],alphabet[i])
