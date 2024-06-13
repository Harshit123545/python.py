class subject:
    def __init__(self,sub1,sub2,sub3,sub4,sub5):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
    def percentage( self):
        per=(self.sub1+self.sub2+self.sub3+self.sub4+self.sub5)/5*100
        if (per>=60 and per<=74):
            print("first div") 
        elif (per>=75):
            print("honor") 
        elif(per<60 and per>=50):
            print("second div") 
        elif(per<50):
            print("third div")
sub1 = int(input("enter first sub marks:"))
sub2 = int(input("enter first sub marks:"))
sub3 = int(input("enter first sub marks:"))
sub4 = int(input("enter first sub marks:"))
sub5 = int(input("enter first sub marks:"))
obj=subject(sub1,sub2,sub3,sub4,sub5)
obj.subject()

