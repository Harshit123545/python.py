list1=[4,5,6,7]
list2=[4,5,8,9]
list3=[4,2,3,0]
s1=set(list1)
s2=set(list2)
s3=set(list3)
com1=s1&s2
result=com1&s3
print("the commom elements among",list1,list2,list3,"are",result)