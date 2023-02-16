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


game=[rock,paper,scissors]



user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"{game[user]}  user choice ")


number=random.randint(0,2)

lenth=len(game)-number

bot=game[lenth]
print(f" {bot} bot choice  ")

first_condition=   user==0 and lenth==2 or user==2 and lenth==1 or user==1 and lenth==0

second_condition= lenth== user

if second_condition :
     print("draw")

if first_condition:
  print("you win :)")


if first_condition or second_condition==False:
        print("you lose :(")

