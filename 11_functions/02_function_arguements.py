def sub(a,b,minus=0):   # a,b are parameters
    # Method1: return a-b
    x = a-b-minus
    return x
c = sub(5,3)   # 5,3 are arguements
print(c)

d = sub(8,3,1)   # 5,3 are arguements
print(d)

e = sub(b=1,a=0)  # I can write these in any order but mention with parameters is a must
print(e)

def student(Name,age):
    print(f"Name:{Name},Age:{age}")
student(age=18,Name="Tanmay Khandelwal")