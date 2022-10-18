from curses.ascii import isdigit
from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
com_num = randint(1,3)

# Turn that random number into the computer's RPS move
com_move = ""
if com_num==1:
    com_move=rock
elif com_num==2:
    com_move=paper
else:
    com_move=scissors    

# Ask a user to enter their move
player_num = input("Choose either number => rock(1), paper(2) or scissors(3)")
if not(player_num.isdigit):
    print("Invalid input, random seletion started...")
    player_num=randint(1,3)
player_num = int(player_num)
player_move=""
if player_num==1:
    player_move=rock
elif player_num==2:
    player_move=paper
else:
    player_move=scissors  
# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("Player:")
print(player_move)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("Com:")
print(com_move)

# Figure out who wins and print the result!
if player_num == com_num:
    print("DRAW!")
elif player_num==1 and com_num==3 or player_num==2 and com_num==1 or player_num==3 and com_num==2:
    print("YOU WIN!!!")
else:
    print("YOU LOSE!!")