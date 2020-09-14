def Str_first2_and_last2(string):
    if len(string)<2:
        return " "
    else:
        return string[0:2]+string[-2:]

string = 'w3resource'
print("string =",string,"with the function:",Str_first2_and_last2(string))
string = 'w3'
print("string =",string,"with the function:",Str_first2_and_last2(string))
string = 'w3w3'
print("string =",string,"with the function:",Str_first2_and_last2(string))
string = 'w'
print("string =",string,"with the function:",Str_first2_and_last2(string))
