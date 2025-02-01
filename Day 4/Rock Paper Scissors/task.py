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

hands = [rock, paper, scissors]


user_played_hands = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n" ))
print(hands[user_played_hands])

bot_played_hands = random.randint(0,2)
print("Computer Choose:")
print(hands[bot_played_hands])

if user_played_hands == 0 and bot_played_hands == 0:
    print("DRAW")
elif user_played_hands == 0 and bot_played_hands == 1:
    print("You Lose")
elif user_played_hands == 0 and bot_played_hands == 2:
    print("You Win")

elif user_played_hands == 1 and bot_played_hands == 1:
    print("DRAW")
elif user_played_hands == 1 and bot_played_hands == 0:
    print("You Win")
elif user_played_hands == 1 and bot_played_hands == 2:
    print("You lose")

elif user_played_hands == 2 and bot_played_hands == 2:
    print("DRAW")
elif user_played_hands == 2 and bot_played_hands == 1:
    print("You Win")
elif user_played_hands == 2 and bot_played_hands == 0:
    print("You Lose")

