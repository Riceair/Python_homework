filename = input("Enter a file name: ")
try:
    file = open(filename)
except:
    print("File cannot be opened:",filename)
    exit()

counts = dict()

for line in file:
    word = line.rstrip()\
           .split()
    if len(word) < 3 or word[0] != "From":
        continue
    counts[word[2]] = counts.get(word[2],0) + 1

print(counts)
    
