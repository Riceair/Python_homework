#先印出第一列的 1~10
print('   ',end=' ') #最一開始的空格
for i in range(1,11):
    print('%3d' % i,end=' ')
print() #換行

for i in range(1,11):
    print('%3d' % i,end=' ') #第一行的 1~10
    for j in range(1,11): #中間部分 剛好為i*j
        print('%3d' % (i*j),end=' ')
    print() #執行完一列，換行
