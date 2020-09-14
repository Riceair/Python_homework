try:
    num_list = []
    while True:
        num = input("Enter an integer (0 to exit): ")
        if num == '0': break
        num = int(num)
        num_list.append(num)
    num_list.sort()
    for n in num_list:
        print(n)
except:
    print("Please enter an integer")
