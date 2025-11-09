# a = input("Enter first number") here when we enter a number it is considered a string so we convert it into integer to add a number
# a = int(a)
# print(a+3)

a = input("Enter first number:")  # here if we need to add and get the sum that is first number 15 and second number is 13 so if we dont convert it into 
a = int(a)                        # int then we will get result as 1513 but if a and b gets converted into int then result will be 28
b = input("Enter second number:")
b = int(b)
print(a + b)

# Now a better way to shorten this above program
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(a + b)