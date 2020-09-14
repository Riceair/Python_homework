import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print("You must provid the file name as a command line parameter.")
    quit()

try:
    in_data = open(sys.argv[1],'r')
    count = 0
    for line in in_data:
        line = line.rstrip()
        print(line)
        count+=1
        if count == 10:
            break
    in_data.close()
except IOError:
    print("An error occurred on reading data.")
