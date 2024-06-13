from typing import Any


class student:
    def __init__(self,rollno,name):
        self.__rollno=rollno
        self.name=name
    def get__rollno(self):             #getter function
        return self.__rollno
    def set__rollno(self,rollno):          #setter function
        self.__rollno=rollno
    def get__name(self):
        return self.name
    def set__name(self,name):
        self.name=name
stu_obj=student(102,"Raghav")
print("before updation")
print(stu_obj.get__rollno())
print(stu_obj.get__name())
stu_obj.set__rollno(103)
stu_obj.set__name("harsh")
print("after updation")
print(stu_obj.get__rollno())
print(stu_obj.get__name())
