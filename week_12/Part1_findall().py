import re
txt = "Danny is a student. He is learning rnn."
x = re.findall("\S+nn\S+",txt)
print(x)
