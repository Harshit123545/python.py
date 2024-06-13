num=int(input("enter a number"))

#if num is greater than 1
if num>1:
    #check if factor exist
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            