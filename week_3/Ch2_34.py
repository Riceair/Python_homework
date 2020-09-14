input_data = input("Please enter an integer: ")
try:
    integer = int(input_data)
    if integer%2 == 0:
        print("Even")
    else:
        print("Odd")
except:
    print("Your input is not an integer!!")
