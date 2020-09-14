def multList(lst):
    ans = 1
    for num in lst:
        ans *= num
    return ans

a_list = [3,6,2,-86,23]
print("a_list =",a_list)
print("multList(a_list) =",multList(a_list))
