def func(my_lst,var1):
    new_lst=[]
    for num in my_lst:
        if(num%var1==0):
            new_lst.append(num//var1)
        else:
            new_lst.append(0)
    return new_lst