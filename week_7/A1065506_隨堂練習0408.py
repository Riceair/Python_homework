string = 'X-DSPAM-Confidence: 0.8475'
index=string.find(':')
number = string[index+1:]
try:
    number = float(number)
    print(number)
except:
    print('something wrong')
