class Area:
    def __init__(self,r,l,b):
        self.radius=r
        self.length=l
        self.breadth=b
    def calArea(self):
        result1=0.5*self.length*self.breadth
        print("Area of triangle is :",result1)
        result2=3.14*self.radius*self.radius
        print("Area of circle is :",result2)
r=int(input("enter radius:"))
l=int(input("enter length:"))
b=int(input("enter breadth:"))
areaobj=Area(r,l,b)
areaobj.calArea()

