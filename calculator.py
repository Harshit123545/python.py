class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def calAdd(self):
        result1=self.num1+self.num2
        print("sum of two numbers:\n",result1)
    def calSub(self):
        result2=self.num1-self.num2
        print("substraction of two numbers:\n",result2)
    def calMul(self):
        result3=self.num1*self.num2
        print("product of two numbers:\n",result3)
    def calDiv(self):
        result4=self.num1/self.num2
        print("division of two numbers:\n",result4)
    def calRem(self):
        result5=self.num1%self.num2
        print("remainder of two numbers:\n",result5)
    def calFloor(self):
        result6=self.num1//self.num2
        print("floor of two numbers:\n",result6)
num1=int(input("enter a number1:"))                                 #object 
num2=int(input("enter number2:"))                                   #object 
calobj=calculator(num1,num2)
calobj.calAdd()
calobj.calSub()
calobj.calMul()
calobj.calDiv()
calobj.calRem()
calobj.calFloor()



