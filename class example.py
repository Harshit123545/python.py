class Employee:
    def __init__(self,id1,name,designation,department,bs):
        self.id1 = id1
        self.name = name
        self.designation=designation
        self.department = department
        self.basicsalary=bs
        self.hra=0
        self.va=0
        self.netsalary=0
    def cal_hra_va_basic(self):
        self.hra=0.3*self.basicsalary
        self.va=0.2*self.basicsalary
        self.netsalary=self.hra + self.va + self.basicsalary

    def display( self):
        print("id = ",self.id1)
        print("name = ",self.name)
        print("designation = ",self.designation)
        print("department = ",self.department)
        print("basicsalry = ",self.basicsalary)
        print("hra = ",self.hra)
        print("va = ",self.va)
        print("net salary = ",self.netsalary)
      

s1 = Employee(101,"Harshit","Web Developer","IT",50000)
s2 = Employee(102,"Himanshu","Programmer","IT",50000)
s3 = Employee(103,"Gaurav","HR","MBA",40000)
s4 = Employee(104,"Divyanshu","Front-end-developer","IT",60000)
s5 = Employee(105,"Yashwant","Back-end-developer","IT",60000)
s1.cal_hra_va_basic()
s1.display()
s2.cal_hra_va_basic()
s2.display()
s3.cal_hra_va_basic()
s3.display()
s4.cal_hra_va_basic()
s4.display()
s5.cal_hra_va_basic()
s5.display()