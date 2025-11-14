coordinates = (10, 20)
print(coordinates)

# we cant modify tuples 

c = list(coordinates)
print(c)
c[0]=50
print(c)
d = tuple(c)
print(d)