try:
    while True:
        temp = input()
        n1 = int(temp.split(' ')[0])
        n2 = int(temp.split(' ')[1])
        theMax = 0
        for i in range(min(n1,n2),max(n1,n2)+1):
            count = 1
            n = i
            while True:
                if n == 1:
                    break
                elif n%2 == 0:
                    n/=2
                else:
                    n = 3*n+1
                count+=1
            theMax = max(theMax,count)
        print(n1,n2,theMax)
except EOFError:
    pass
print()
