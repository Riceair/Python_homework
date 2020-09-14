cdict=dict()
string = input("Enter a string: ")
for s in string:
    cdict[s]=True
print("That string contained",len(cdict),"unique character(s).")
