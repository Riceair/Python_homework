level = input("Please input the decibel level: ")
noiseName = ['Jackhammer','Gas lawnmower','Alarm clock','Quiet room']
noiseLevel = [130,106,70,40]
try:
    level = float(level)
    if level > noiseLevel[0]:
        print('The level is larger than the loudest level table!!')
    elif level < noiseLevel[3]:
        print('The level is smaller than the quietest noise in the table!!')
    else:
        for i in range(len(noiseLevel)):
            if level == noiseLevel[i]:
                print('The level is ',noiseName[i])
                break
            elif noiseLevel[i+1] < level < noiseLevel[i]:
                print('The level is between ',noiseName[i],' and ',noiseName[i+1])
                break
except:
    print("Please input a level")