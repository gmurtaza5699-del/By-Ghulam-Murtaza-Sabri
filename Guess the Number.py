from math import *
import random

num = random.randrange(1, 101) # Call Random Number
print(f'Ghulam Murtaza Python//<.>& C:/Users/cbla_students/AppData/Local/Programs/Python/Python313/python.exe {num}Import-Module PSReadLine')
head1=(":Guess the Number (1 to 100):") # Heading 1
print(head1.center(150))


head=(":Press 'Enter' to start the Game:") # Heading 2
print(head.center(60))
user = input("Press Enter ") # Enter Button


"""if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")"""

for a in range(1,6):                # Take a Numbers From User using Loop````
    guess = int(input(" Guess Number (1 to 100): ")) 

    if  guess == num:  # User Number Matchng
        print('You Won 🏆')
        break                       # break if you guess number game is finished
    elif guess<num:
        print("too low")
    else:
        print("too high")
else:
    print(f"You Lost. The correct number was {num} ❌") # Wrong Condition

