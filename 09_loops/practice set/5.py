a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = input("Enter the operation you want to have between a and b (+, -, *, /, %): ")

match c:
    case "+":
        print("The addition of a and b is:", a + b)
    case "-":
        print("The subtraction of a and b is:", a - b)
    case "*":
        print("The multiplication of a and b is:", a * b)
    case "/":
        print("The division of a and b is:", a / b)
    case "%":
        print("The remainder when a is divided by b is:", a % b)
    case _:
        print("No valid operator selected.")
