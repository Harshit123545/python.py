class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.__name=name
    def display(self):
        print(self.rollno)
        print(self.__name)
s1=student(5,"Harshit")
s1.display()
print(s1.rollno)
print(s1._student__name)