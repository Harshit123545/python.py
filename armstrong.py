n = int(input("enter a number"))
s=n
sum1 = 0
while n!=0:
    r =  n % 10
    sum1=sum1+(r**3)
    n=n//10
if s == sum1:
    print("the given number",s,"is armstrong number")
else:
    print("the given number",s,"is not an armstrong number")



    # 1,2,3,4,5,6,7,8,9,153,370,407,  armstrong number are those number 