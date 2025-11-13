import my_utils

num = int(input("Enter a number: "))

if my_utils.is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")


def safe_divide(a, b):
    if b==0:
        print("cannot divide by 0")
        return # stops the function my mistake
    c =  a/b
    print(c)
safe_divide(3,0)  # my mistake in this code is that instead of , i have written /
safe_divide(3,1)
safe_divide(3,2)
safe_divide(3,3)

def fib(n):
    if n == 0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(9))
print(fib(19))
print(fib(15))