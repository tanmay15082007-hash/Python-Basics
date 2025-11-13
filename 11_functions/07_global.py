def sum(a,b):
    print("I am summing.")
    c = a+b
    global z # please modify global z
    z = 0 # This will refer to global z and will not create a local variable
    return c

z=3  
print(sum(3,12))
print(z)  # means at output we will have the value of z which is inside the defined functioN as it is will act as global variable