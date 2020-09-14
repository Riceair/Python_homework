#exercise 6
def computepay(hours,rate):
    try:
        hours = float(hours)
        rate = float(rate)
        if hours>=40:
            pay = 40*rate + (hours-40)*rate*1.5
        else:
            pay = hours*rate
        return pay
    except:
        print('Please input number!!')

hours = input('Please input hours: ')
rate = input('Please input rate: ')
pay = computepay(hours,rate)
print(pay)
