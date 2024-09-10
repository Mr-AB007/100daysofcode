#ROCK PAPER SCISSORS GAME
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock,paper,scissors]
userChoice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comChoice = random.randint(0,2)

if  userChoice < 0 or userChoice > 2:
    print("Invalid Input, You lose")
else:
    print(choices[userChoice])
    print(f"Computer Chose\n{choices[comChoice]}")

if userChoice == 0 and comChoice == 2:
    print("You win")
elif userChoice == 2 and comChoice == 0:
    print("You lose")
elif userChoice == 1 and comChoice == 0:
    print("You win")
elif userChoice == 0 and comChoice == 1:
    print("You lose")
elif userChoice == comChoice:
    print("It's Draw")