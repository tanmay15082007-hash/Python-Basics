'''
IN THIS METHOD WE CHECK MANUALLY NOT FEASIBLE 
a = input("Enter a word:\n").lower()
b = len(a)
if (b%2==0):
    if(a[0]==a[-1] and )
    '''

a = input("Enter a word:\n").lower()
if(a == a[::-1]):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")