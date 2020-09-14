def reverseString(string):
    return ''.join(reversed(string))
#reversed(string)會產出反轉的list，用join可合併成字串

string = "abc123"
print("string =",string,"with the function:",reverseString(string))
string = "Danny is a dog."
print("string =",string,"with the function:",reverseString(string))
