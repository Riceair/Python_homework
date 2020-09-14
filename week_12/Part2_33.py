import re
text = "Hello world abc123 lazy Danny dog"
print(re.findall("[A-z]{5}",text))
