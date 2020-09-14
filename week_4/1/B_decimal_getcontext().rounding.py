from decimal import*
getcontext().prec=3
print('prec=3')
getcontext().rounding = ROUND_HALF_EVEN
print('Decimal(\'3.141\')+Decimal(\'2.713\'),rounding=ROUND_HALF_EVEN -> ',Decimal('3.141')+Decimal('2.713'))
getcontext().rounding = ROUND_UP
print('Decimal(\'3.141\')+Decimal(\'2.713\'),rounding=ROUND_UP -> ',Decimal('3.141')+Decimal('2.713'))
