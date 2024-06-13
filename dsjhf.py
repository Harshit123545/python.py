l1=['A',0,1,2,'B','C',0,4]
L2=list()
l3=list()
for i in l1:
    if(i>=0 and i<=9):
        L2=L2.append(i)
    else:
        l3=l3.append(i)
print(L2)
print(l3)