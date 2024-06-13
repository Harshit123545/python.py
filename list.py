
#list1=[2,3,5,7,8]
#sum1=0
#for ele in list1:
 #   sum1=sum1+ele
#print("the summesion of all elements is",sum1)

list=[]
print("enter size")
n=int(input())
sum1=0
for i in range(n):
    element=int(input("enter list element"))
    list.append(element)
print(sum(list))

