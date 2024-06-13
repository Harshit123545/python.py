# str1=input("enter) a string")
# str2=str1[::-1]
# if str1==str2:
#     print("pallindrome string")
# else:
#     print("not pallindrome string")





# write a python program o get a single string from two given strings,
# seperated by a space and swap the first two characters of each string


a = 'hello'
b = 'psit'
print("Before Swap :",a," ",b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print("After Swap :",a1," ",b1)