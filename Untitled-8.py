class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
n = int(input("enter a number"))
t = int(input("enter a number 2"))
obj1= A(n)
obj2= A(t)
if(obj1>obj2):
    print("obj1 is grater than obj2")
else:
    print("obj2 is greater than obj1")
