#write a python programme to find greatest no. among three number using if elif else ladder

num1=int(input("enter first number"))  
num2=int(input("enter second number")) 
num3=int(input("enter third number"))
if num1>num2 and num1>num3 :
    print("the greater number is ",num1)
elif num2>num3 and num2>num1:
    print("the greatest number is ",num2)
elif num3>num1 and num3>num2:
    print("the greatest number is",num3)
else:
    print("wrong input")