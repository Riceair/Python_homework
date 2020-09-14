file = input("請輸入檔名: ")
try:
    file = open(file)
    sender = dict()
    for line in file:
        if line.startswith("From "):
            lst = line.split()
            if len(lst) >= 2:
                sender[lst[1]]= sender.get(lst[1],0)+1

    lst = [(val,key) for key,val in sender.items()]
    lst = sorted(lst,reverse=True)
    c,name = lst[0]
    print(c,name)
except:
    print("Can't open the file")
