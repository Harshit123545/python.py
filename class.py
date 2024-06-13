#demonstration of class
class Employee:
    def _init_(self):
        print("inside constructor")
    def display(self):    #behaviour of object
        print("Hello first method")
    def result(self):  #behaviour of object
        print("Hello second method")
demoobj=Demo() #object creation
demoobj.display()   #accessing class member
demoobj.result()    #accessing class member