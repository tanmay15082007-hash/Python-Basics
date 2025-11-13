'''
def add(a,b):
    # a and b are local variables as we cant access them outside the function definition
    c = a+b
    print(z)
    return c

z = 10 # z is a global variable as we can access this from anywhere
print(add(3,4))

'''
def add(a,b):
    # a and b are local variables as we cant access them outside the function definition
    c = a+b
    z = 1 # it creates a new local variable z which destroys when the function is retuned
    print(z) # but here we can clearly see that if 2 variables name is same and in output of the fnc when print z in 2 different places output is 2 diff values of z
    return c

z = 10 # z is a global variable as we can access this from anywhere
print(add(3,4))
print(z)

