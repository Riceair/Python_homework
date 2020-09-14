def is_even(n):
    return n%2 == 0

newList = [1,2,3,4,5,6,7,8,9]
print('newList = ',newList)
print('list(filter(is_even,newList)) = ',list(filter(is_even,newList)))
