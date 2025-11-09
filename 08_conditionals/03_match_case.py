a = int(input('Enter your number written on your lottery ticker which is between 1 to 10: '))

match a:
    case 1:
        print('You won a car')
    case 10:
        print('You won a charger')
    case 7:
        print('You are a f****. Now you owe me $100')
    case 9:
        print('You won a bumper package of $90,000')
    case _:
        print('Better luck next time')
