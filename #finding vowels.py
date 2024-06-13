#finding vowels
#list1={'a','e','i','o','u','A','B','E','I','O','U'}
set_vov=set("aeiouAEIOU")
str1=input("enter a string")
count=0
for i in str1:
    if i in set_vov:
        count=count+1
print("count of vowels in ",str1,"is",count)