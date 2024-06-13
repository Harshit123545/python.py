# a={1,2,5,4,7,8,'r','s'}
# b=frozenset(a)
# print(b)

# fset=frozenset({4,6,9})
# print(type(fset))
# fset.add(87)

a=frozenset({1,2,3,4})
b=frozenset({3,4,5,6})
c=a.copy()
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
