integer=0
factor=2

integer = input('Enter an integer (2 or greater): ')
try:
    integer = int(integer)
    if integer < 2:
        print('Invalid input')
    else:
        while integer>1:
            if integer%factor == 0:
                print(factor)
                integer/=factor
            else:
                factor+=1
except:
    print('Invalid input')
