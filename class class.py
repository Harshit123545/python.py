class student:
    def __init__(self):
        self.name = None
        self.roll_number=None
        self.id=20
    def display_name(self,roll_number,name):
        self.roll_number=roll_number
        self.name=name
        print(self.roll_number,self.name)
s1 = student()
s1.display_name(12,"Harshit")  
s2 = student() 
s2.display_name(15 , "Arvind")     