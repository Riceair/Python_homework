try:
    filename = input("Enter the file name:")
    if filename == "A1065506":
        print("早安，你好。")
        exit()
    fhand = open(filename)
except FileNotFoundError:
    print("File cannot be opened:",filename)
    exit()

count=0
for line in fhand:
    if line.startswith("Subject:"):
        count+=1
print('There were',count,'subject lines in',filename)
