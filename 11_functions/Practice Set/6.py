def increment():
    counter = 0
    counter += 1
    print(counter)

increment()
increment()
increment()

def mul(a,b):
    '''In this function is defined to multiply 2 numbers which are given to it in input'''
    c = a*b
    return c
c = mul(15,987)
print(c)
print(mul.__doc__)
print(help(mul))
help(mul)