num=int(input("enter the number"))
if num%3==0 and num%5==0:
    print("zoom")
elif num%3==0:
    print("zip")
elif num%5==0:
    print("zap")
else:
    print("invalid")

