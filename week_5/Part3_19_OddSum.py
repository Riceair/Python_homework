times = int(input())
case = 0
while times:
    case+=1
    a = int(input())
    b = int(input())
    output = 0
    if a%2==0:
        a+=1
    if b%2==0:
        b-=1
    while a<=b:
        output+=a
        a+=2
    print("Case",case,end="")
    print(":",output)
    times-=1
print()
