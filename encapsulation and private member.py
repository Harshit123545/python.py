class Student:
    def __init__(self,rollno,name):
        self.__rollno=rollno  #self.__rollno is a private
        self.name=name  #self.name is public
    def display(self):
        print(self.__rollno)
        print(self.name)
s1=Student(23,"Harshit")
s1.display()
print(s1.name)  #correct
print(s1.__rollno)  #error