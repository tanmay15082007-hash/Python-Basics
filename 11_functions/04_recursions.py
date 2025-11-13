'''
   0 1 1 2 3 5 8 13 
   0 1 12 3 4 5 6 7 ......
fib(0)=0
fib(1)=1
fib(2)=fib(0)+fib(1)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3)
fib(5)=fib(3)+fib(4)
fib(n)=fib(n-2)+fib(n-1)

'''

def fib(n):
    if (n==0 or n==1):
        return n
# Here in this line we can't use direct c =  fib(n-2)+fib(n-1) and in next line return 0 as we haven't defined what is fib(n) so it will not be correct but when we used simple add(x,y) it is correct as it is predefined x,y as variables
    return fib(n-2)+fib(n-1) 

c = fib(1)
print(c)
d=fib(8)
print(d)
e=fib(19)  # In this for getting the value of e it will take much time but instead of 90 we take 19 it will 10 seconds
print(e)