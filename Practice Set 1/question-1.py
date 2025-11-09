print('Hello, world! Welcome to python')

print("Twinkle, twinkle, little star,\nHow I wonder what you are!")

print('''
Twinkle, twinkle, little star,
How I wonder what you are!
      ''')

print('''
     Twinkle, twinkle, little star,
     How I wonder what you are!
      ''')

name = "Tanmay Khandelwal"
age = 18
is_student = 'True'
height = 161

# As we can see that in below code we should have all elements in str so we convert int to string
'''
print('I am '+ name +'.My age is'+ age +'years old.'+'My height is'+ height +'cms.'+'Student: '+ is_student)
'''
print('I am '+ name +'.My age is '+ str(age) +' years old.'+'My height is '+ str(height) +' cms.'+' Student: '+ is_student)

num = "45"
b = int(num)
print(b+15)
print(int(num)+15) # A better method as compared to previous one
'''
a = input("Enter your favourite food: ") # Both orientation and asking of questions is different but most suitable is second one
print("WOw I also like this " + a)

a = input("Enter your favourite food:\n")
print("WOw I also like this " + a)

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
print(a+b)
print(a-b)
print(a/b)
print(a//b)
'''
print('Harry said, "Python is awesome!"\nThis is on a new line.\nThis is a tab ->\t <- here')

a = int(input('Enter your number:\n'))

print('Square is:',a**2)
print('Cube is:',a**3)

