a = int(input("Enter a number:\n"))
if a<0:
    print("The number is negative.")
elif a%2==0:  # here we cant write if we change it to elif as in case of -89 it gives 2 output i.e number is negative and number is odd
    print("The number is even.")
elif a==0:   # Here we cant write a==0 condition before a%2==0 because 0%2==0 is True so it will print number is even for 0
    print("The number is neither even nor odd.")
else:
    print("The number is odd.")