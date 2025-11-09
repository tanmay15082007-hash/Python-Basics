print('Hello champs, good morning. Wake up and grind like that your world depends on it. That after your all hard work,you are on top of food chain.')
print("Hello Tanmay. I am your personalised alarm system. According to your settings you should wake up.Otherwise I would have to initiate alpha protocol.")

#a = ('Tanmay','Khandelwal',18,'top of the world')
#b = (Hello I am %s %s. I am %s years old. Currently I am nothing. I have fallen "from" grace. I can't even live a hour even without thinking porn.My weight is currently increasing like the world is ending.I have no control over my eating habits whatsoever.But in next 4 years I promise to myself that I will be someone who others envy.Remember girls will come in your way to the excellence.Today i was asking about a girl like she was my crush even if she was my classmate. She also know that I am a batchmate of her. She could have also approached me.)
#     print(a % b)

# see where you were wrong.This will come in list at site learnpython.org

a = "Tanmay Khandelwal"
b = 34
c = True
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

'''
d = 34
e = print(str(d))
print(type(e))
print(e)
'''

a = 34
b = str(a)
print(b)
print(type(b))
'''
c = int(input("Enter your first number: "))
d = int(input("Enter your second number: "))
print(c + d)       

a = input("Enter your first number: ")
b = input("Enter your second number: ")
print(a + b)
'''
print('I am Tanmay Khandelwal.\n I seen my classmates so much ahead of me.\n I have too much ahead to work on me.\n But when Tanmay Khandelwal decides he will do it then it means he will do it.\n No one will come in my way.')

print('I am Tanmay Khandelwal.\tI will conquer myself')

print("Tanmay",'Khandelwal',18, sep = ',')
print("Tanmay",'Khandelwal',18, sep = ' ')

age = 18
print('I am Tanmay Khandelwal.', end = ',')
print('I am %d years old.' % age)

age = 18
print("I am Tanmay Khandelwal", end='.')
print('I am %d years old.' % age)

a = ("John", "Doe", 53.44)
format_string = ('I am %s %s.I have currently $%s .')
print(format_string % a)

a = ('Tanmay Khandelwal',18,'millionaire',30)
b = ('I am %s.I am currently %s years old.I will be a %s by the age of %s')
print(b % a)

a = 34
b = 2
print(a + b)
print(a - b)
print(a ** b)
print(a * b)
print(a // b)
print(a % b)

a = 'Tanmay'
print(type(a) == str)

b = 34
print(type(b) == int)
print(b>4)
print(b<4)
print(b == 4)
print(b<=34)
print(b>=34)
print(b!=34)

# Here we will get error while running the code as we have not converted the a string input to integer
'''
a = input('Enter your age: ')
print(a)
if (a>18):
    print('You are too young to donate blood.')
elif(a == 18):
    print('You have just turned 18.If we don\'t have any above age tier volunteers, then you will be called.')
else:
    print('You are currently too young to donate blood.')
'''

# Now the corect part (But a problem faced if we write the age 18.0 then it shows error what to do to include integer based answers in it as well)
a = int(input('Enter your age: '))
print(a)
if (a>18):
    print('You are too young to donate blood.')
elif(a == 18):
    print('You have just turned 18.If we don\'t have any above age tier volunteers, then you will be called.')
else:
    print('You are currently too young to donate blood.')

a = int(input('All the chits with number are here.A random person will pick a chit and whose number will be there he will give the speech first and so on: '))

match a:
    case 5:
        print('You are the first person.')
    case 8:
        print('You will be the second person.')
    case 2:
        print('You will be the third person.')
    case _:
        print('Rest lectures by person will be tomorrow.It will be mailed to your student college id.')
# Here I experimented a bit and wrote 3 commands in succession of print.Now we can see in the result that it completes first part of command 1, then second part of command 2 and then the third part
for i in range(1,10):
    print(i)
    print(i*5)
    print(20*(i))