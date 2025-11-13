a = 4
b=2
c=1
avg = (a+b+c)/3
print(avg)

def average(a,b,c):
    d = (a+b+c)/3
    print(d)
average(3,5,6)
o1=average(3,5,6)
print(o1)                # Here in print(o1,o2) no output will be received as when defining the function we have not the value returned. So to have the value stored see hte below code
average(5,7,8)
o2=average(5,7,8)
print(o2)
def avge(a,b,c):
    d = (a+b+c)/3
    return d

d1=avge(100,5,6)
d2=avge(10,5,607)
print(d1,d2)



def name(e,f):
    print(f"I am {e}. I got {f} marks.")
name("Tanmay Khandelwal",99)

def name(e):
    print(f"I am {e}.")
name("Tanmay Khandelwal")
