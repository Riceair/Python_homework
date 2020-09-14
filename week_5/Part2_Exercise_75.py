try:
    n = int(input('Enter a positive integer: '))
    m = int(input('Enter a positive integer: '))
    if n<0 or m<0:
        print('Invalid input')
    else:
        the_n = n
        the_m = m
        while n != m:
            if n > m:
                n-=m
            elif m > n:
                m-=n
        print('The greatest common divisor of',the_n,'and',the_m,'is',n)
except:
    print('Invalid input')
