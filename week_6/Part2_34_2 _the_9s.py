while True:
    N = input()
    if int(N) ==0:
        break
    count = 0
    for i in N:
        count+=int(i)
    n = 0
    degree = 0
    while True:
        if count%9 != 0:
            break
        elif count==9:
            degree+=1
            break
        else:
            degree+=1
            n=count
            count=0
            while n % 10 != 0:
                count+= n%10
                n//=10
    if degree > 0:
        print(N,'is a multiple of 9 and has 9-degree',degree,end='')
        print('.')
    else:
        print(N,'is not a multiple of 9.')
print()
