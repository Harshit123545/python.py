a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)

n1=['geny','bear','charlaton','daman']
n2=n1
n3=n1[:]
n2[0]='alice'
n3[1]='bob'
sum=0
for ls in(n1,n2,n3):
    if ls[0]=='alice':
        