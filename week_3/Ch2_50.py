print('請輸入一元二次方程式的a,b,c(ax^2+bx+c=0)')
try:
    a = input('請輸入a(不得為0): ')
    a = float(a)
    if a == 0:
        print('a不得為0!!')
    else:
        b = input('請輸入b: ')
        b = float(b)
        c = input('請輸入c: ')
        c = float(c)
        if b**2 - 4*a*c < 0:
            print('根的數量為 0 -> 無解')
        elif b**2 - 4*a*c == 0:
            print('根的數量為 1 -> 重根: ',(-1*b)/(2*a))
        else:
            print('根的數量為 2 -> 兩解: ',((-1*b)+(b**2 - 4*a*c)**(1/2))/(2*a),', ',((-1*b)-(b**2 - 4*a*c)**(1/2))/(2*a))
except:
    print('請輸入數字!!')