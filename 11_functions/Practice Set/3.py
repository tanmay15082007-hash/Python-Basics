'''
add = lambda a,b:a+b
print(add(3,10))

square = lambda c:[c*c for c in range(1,6)]
print(square(0))
'''
square = lambda x:x*x
num = [1,2,3,4,5]
print(list(map(square,num)))