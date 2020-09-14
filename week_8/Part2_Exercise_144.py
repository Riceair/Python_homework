try:
    filename = input("Please input the filename: ")
    read_file = open(filename,'r')
    out_filename = "numberlines_"+filename
    out_file = open(out_filename,'w')
    count = 1
    for line in read_file:
        outline = str(count)+": "+line
        out_file.write(outline)
        count+=1
    read_file.close()
    out_file.close()
except IOError:
    print("An error occurred.")
