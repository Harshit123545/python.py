# # a = True
# # b = False
# # c = True
 
# # if not a or b:
# #     print ("a")
# # elif not a or not b and c:
# #     print ("b")
# # elif not a or b or not b and a:
# #     print ("c")
# # else:
# #     print ("d")


# x = "abcdef"
# i = "i"
# while i in x:
#     print(i, end=" ")

tuple = {} 
tuple[(1,2,4)] = 8
tuple[(4,2,1)] = 10
tuple[(1,2)] = 12
_sum = 0
for k in tuple: 
    _sum += tuple[k] 
print(len(tuple) + _sum)