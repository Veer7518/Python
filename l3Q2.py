list2=[1,2,3, 4]
#list1 =[1,2,3]
#list1.reverse()
copy_list2 = list2.copy()
list2.reverse()
if (copy_list2 == list2):
    print("It is palindrome")
else:
    print("It is not palindrome")

print(list2)