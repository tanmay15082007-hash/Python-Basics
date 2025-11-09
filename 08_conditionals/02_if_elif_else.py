age = int(input('Enter your age: '))

if(age>18):
    print('You can drive.')
elif(age==18):
    print('Let\'s schedule an interview')
elif(age==0):
    print('You are just born. Why are you trying to drive a car?')
else:
    print('Sorry, you can\'t drive.')
