def factorial(n):
    if (n== 0 or n==1):
        return 1
    return n*factorial(n-1)

c = factorial(10)
print(c)

def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)  # remainder that is last digit + number n with its last digit chopped off that it is integer division  
c = sum_of_digits(213)
print(c)