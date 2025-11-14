my_set = {1, 2, 3, 3, 4}
print(my_set) # in output 3 will be print only one time as in set there are onlu unique elements print and the dulicate elements only get printed one time
my_set.add(5)
my_set.remove(2)
print(my_set)

a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
d = a.intersection(b)
e = a.difference(b)
print(c,d,e)