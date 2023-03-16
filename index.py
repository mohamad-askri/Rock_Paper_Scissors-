'''
Rock Paper Scissors game v2.

'''

import random

table = {
    "rock": { "rock": 0,  "paper": -1,   "scissors": 1},
    "paper": { "rock": 1,   "paper":0,   "scissors":-1},
    "scissors": {"rock": -1,   "paper":1,   "scissors": 0}
}

choices = ["rock", "paper", "scissors"]

while (True):
    user_choice = int(input("Rock, paper, scissors? (1,2,3) "))
    if (user_choice in [1,2,3]):
        break

user_choice = choices[user_choice-1]
bot_choice = random.choice(choices)

print(f"You: {user_choice}")
print(f"Bot: {bot_choice}")

result = table.get(user_choice).get(bot_choice)

if result==0:print("tied game")
elif result==1:print("win")
elif result==-1:print("lost")