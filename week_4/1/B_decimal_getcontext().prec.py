from decimal import*
getcontext().prec = 6
print('prec=6,Decimal(1)/Decimal(7)= ',Decimal(1)/Decimal(7))
getcontext().prec = 28
print('prec=28,Decimal(1)/Decimal(7)= ',Decimal(1)/Decimal(7))
