#!/usr/bin/python3

'''A rock, paper, scissors game.'''
'''
The Rules:
The outcome of the game is determined by 3 simple rules: 
 Rock wins against scissors.
 Scissors win against paper.
 Paper wins against rock.

'''
import random
import time


random.seed(time.time())

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

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
choices = [rock, paper, scissors]
computer_choice = random.choice(choices)

# print the player ASCII
if player == 0:
	print(rock)
elif player == 1:
	print(paper)
elif player == 2:
	print(scissors)
else:
	print('You are wrong !')

#print the computer ASCII
print("Computer chose:")
print(computer_choice)


# -1 : means lose
#  0 : means equal
#  1 : means win

#         Rock Paper Scissors
#Rock       0    -1      1
#Paper      1     0     -1
#Scissors  -1     1      0 


computer_rock = [ 0,-1, 1]
computer_paper = [ 1, 0,-1]
computer_scissors = [-1, 1, 0]

# print the result 
result = 0
if computer_choice == rock:
	result = computer_rock[int(player)]
elif computer_choice == scissors:
	result = computer_scissors[int(player)]
elif computer_choice == paper:
	result = computer_paper[int(player)]


if result == 0:
    print("Equal")
elif result == -1:
    print("You win!")
else:
    print("You lose!")
