people = input('請輸入人的數目: ')
dogYear = 0
try:
    people = float(people)
    if people >= 0:
        if people <= 2:
            dogYear = people * 10.5
        else:
            people-=2
            dogYear = people*4 + 10.5*2
        print('換算成狗的壽命為: ',dogYear)
    elif people < 0:
        print('請輸入正數')
except:
    print('請輸入正數')