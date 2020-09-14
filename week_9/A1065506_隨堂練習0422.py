numlist = []
try:
    while True:
        number = input("Enter a number: ")
        if number == "done":
            break
        number = float(number)
        numlist.append(number)
    print("Maximum:",max(numlist))
    print("Minimum:",min(numlist))
except:
    print("請輸入數字")
