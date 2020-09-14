import re
exp = input("Enter a regular expression: ")
count = 0
file = open("mbox.txt")
for line in file:
    x = re.findall(exp,line)
    if x != []:
        count+=1
    
print("mbox.txt had",count,"lines that matched",exp)
