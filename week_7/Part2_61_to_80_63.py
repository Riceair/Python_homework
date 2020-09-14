def removeLeading0(string):
    split_string = string.split(".")
    string = ".".join(str(int(s)) for s in split_string)
    return string

ip="192.128.018.011"
print("IP =",ip)
print("with the function:",removeLeading0(ip))
ip="127.0.0.1"
print("IP =",ip)
print("with the function:",removeLeading0(ip))
