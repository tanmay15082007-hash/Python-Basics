a = {1,2,3,4,5,6,7,15}
b = {7,8,9,10,11,12,14,15}
c = a.union(b) # contain all elements of a along with b
print(c)

d = a.intersection(b)  # CONTAINS ONLY THE ELEMENTS OF A THAT ARE ALSO PRESENT IN B
print(d)

e = a.difference(b)  # it removes the elemnts present in a which are present in b
print(e)

