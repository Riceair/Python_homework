try:
    file = input("Please input the filename: ")
    rf = open(file,'r')
    cf = open("copy_"+file,'w')
    for line in rf:
        cf.write(line)
    rf.close()
    cf.close()
except IOError:
    print("An error occurred")
