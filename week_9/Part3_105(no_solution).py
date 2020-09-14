lst = []
while True:
    data = input("Please enter something (0 to exit):")
    if data == '0': break
    lst.append(data)
lst.reverse()

for data in lst:
    print(data)
