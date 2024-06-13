#write a python program to calculate net salary if basic salary is 20,000 hra is 35% of basic salary and way is 20% of basic salary
def net_salary(basic_salary):   #func signature  #formal parameters
    hra=35/100*basic_salary
    va=20/100*basic_salary
    net=basic_salary+hra+va
    return net
basic_salary=int(input("enter basic salary"))
net=net_salary(basic_salary)   #function call  #actual parameter
print("the employee net salary is",net)


    