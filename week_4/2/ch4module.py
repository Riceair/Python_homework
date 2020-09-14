import math
def factorial(n):
    try:
        n = int(n)
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            return n*factorial(n-1)
    except:
        print('Please input a number')

def degree2radian(d):
    try:
        d=float(d)
        return d*(math.pi/180)
    except:
        print('Please input a number')
