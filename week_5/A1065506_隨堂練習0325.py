maximum=None
minimum=None
total=0.0
count=0

while True:
    input_num = input('Enter a number: ')
    if input_num == 'done':
        break;
    try:
        input_num = float(input_num)
    except:
        print('Invalid input')
    else:
        total += input_num
        count += 1
        if maximum is None or input_num > maximum:
            maximum=input_num
        if minimum is None or input_num < minimum:
            minimum=input_num
print(total,count,maximum,minimum)
