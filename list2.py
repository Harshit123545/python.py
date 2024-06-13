list1=[7,8,100,5]
print(max(list1))
max1=list1[0]
for i in range(1,len(list1)):
     if i < max1:
             max1 = i
    
print("the greatest element is:",max1)