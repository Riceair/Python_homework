textdict = {
    1:".,?!:",
    2:"ABC",
    3:"DEF",
    4:"GHI",
    5:"JKL",
    6:"MNO",
    7:"PQRS",
    8:"TUV",
    9:"WXYZ",
    0:" "
}
number = input("Please the number sequence:")
current = number[0] #紀錄目前的數字
count=0 #紀錄目前數字出現次數
first=True #確認現在是否為第一個字
out=""
for n in range(len(number)):
    if current == number[n]:
        count+=1
    elif current != number[n]:
        count = count%len(textdict[int(current)])
        if first:
            out+=textdict[int(current)][count-1]
            first=False
            current = number[n]
            count=1
        elif out[-1] == '0':
            out+=textdict[int(current)][count-1]
            print(textdict[int(current)][count-1])
            current = number[n]
            count=1
        else:
            out+=textdict[int(current)][count-1].lower()
            current = number[n]
            count=1
count = count%len(textdict[int(current)])
out+=textdict[int(current)][count-1].lower()
current = number[n]
print(out)
