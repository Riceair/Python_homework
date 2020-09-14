import re
def text_match(text):
    string = "ab+"
    if re.search(string,text):
        return "Found a match!"
    else:
        return "Not matched!"
print(text_match("ab"))
print(text_match("abbc"))
print(text_match("ac"))
