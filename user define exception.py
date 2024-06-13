class SalaryNotinRangeError(Exception):
    pass
try:
    emp_name=input("enter name")
    Salary=int(input("enter salary:"))
    if Salary<20000 or Salary>50000:
        raise SalaryNotinRangeError
    else:
        print("employee name:",emp_name)
        print("salary is range")
except SalaryNotinRangeError:
    print("employee name:",emp_name)
    print("salary is not applicable",emp_name)