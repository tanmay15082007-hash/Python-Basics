power = lambda x:x*x
'''
 As good as writing
     def power(x):
        return x*x
     
'''
print(power(3))
print(power(4))

sum = lambda x,y:x+y
'''
 As good as writing
     def sum(x,y):
        return x+y
     
'''
print(sum(3,4))

subtract = lambda x,y:x+y
print(subtract(17,-9))

multiply = lambda x,y:x*y
print(multiply(3,4))

division = lambda x,y:x/y
print(sum(15,6))

add = lambda y:[y+i for i in range(1,11)]
print(add(7))

multiply = lambda y:[y*i for i in range(1,11)]
print(multiply(7))