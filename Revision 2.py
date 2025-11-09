print('Hello " World')
print('I','am','Tanmay', sep = ' ')
print('I','am','Tanmay', sep = '..')
print('I','am','Tanmay', sep = '/')
print('I','am','Tanmay', sep = '*')
print('I','am','Tanmay', sep = ' ', end='? ')
print('Pro Player')



# Here we can see that in both cases if in default case any no we give it will return as it is here there is no point of loop command as it print whatever is there in default case.
kills = int(input('Enter the number of kills done in a single match: '))
match kills:
    case 0:
        print('You are noob. Go practice more on your kills.')
    case _: 
        kills in range(1,6)
        print('You are a good player.')
        


kills = int(input('Enter the number of kills done in a single match: '))
match kills:
    case 0:
        print('You are noob. Go practice more on your kills.')
    case _: 
        kills in range(1,6)
        print('You are a good player.')
        kills in range(6,11)
        print('You are a pro player.')

# Here in below 2 sentences there is one difference of space in code so as we can observe in the result that there is one difference of space
print('I am Tanmay\t Khandelwal')
print('I am Tanmay\t Khandelwal')
    

