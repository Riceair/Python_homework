def strip_char(string,chs):
    return "".join(c for c in string if c not in chs)

string = "Danny is not a dog."
print("string =",string)
strip_string = "aotg"
print("the striped characters:",strip_string)
print("with the function:",strip_char(string,strip_string))
