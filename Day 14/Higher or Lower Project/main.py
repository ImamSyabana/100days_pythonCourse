import game_data
import art
import random


paramterLanjut = True
score = 0

idx1 = random.randint(0, len(game_data.data) - 1)
idx2 = random.randint(0, len(game_data.data) - 1)

while paramterLanjut == True:

    if score > 0:
        print("You're right! Current Score: {nilai}".format(nilai = score))

    print(art.logo + "\n")


    while (idx1 == idx2):
        idx2 = random.randint(0, len(game_data.data)-1)


    print("Compare A: {name}, a {desc}, from {state}.".format(name = game_data.data[idx1]["name"], desc = game_data.data[idx1]["description"], state = game_data.data[idx1]["country"] ))

    print("{logoVS}".format(logoVS = art.vs))

    print("Against B: {name}, a {desc}, from {state}.".format(name = game_data.data[idx2]["name"], desc = game_data.data[idx2]["description"], state = game_data.data[idx2]["country"] ))

    answerAB = (str(input("Who has more followers? Type 'A' or 'B': "))).upper()

    while (answerAB != 'A' and answerAB != 'B'):
        print("\nEnter only 'A' or 'B' !!!")
        answerAB = (str(input("Who has more followers? Type 'A' or 'B': "))).upper()
        if answerAB == 'A' or answerAB == 'B':
            break

    if answerAB == 'A' and game_data.data[idx1]["follower_count"] > game_data.data[idx2]["follower_count"]:
        score = score + 1 # karena bener dapet poin satu
        idx1 = idx2
        idx2 = random.randint(0, len(game_data.data) - 1)

    elif answerAB == 'A' and game_data.data[idx1]["follower_count"] < game_data.data[idx2]["follower_count"]:
        print("Sorry, that's wrong. Final score: {nilai}".format(nilai = score))
        paramterLanjut = False

    elif answerAB == 'B' and game_data.data[idx1]["follower_count"] < game_data.data[idx2]["follower_count"]:
        score = score + 1
        idx1 = idx2
        idx2 = random.randint(0, len(game_data.data) - 1)

    elif answerAB == 'B' and game_data.data[idx1]["follower_count"] > game_data.data[idx2]["follower_count"]:
        print("Sorry, that's wrong. Final score: {nilai}".format(nilai=score))
        paramterLanjut = False

    print("\n "*30)
# print("Compare A: {name}, a {desc}, from {state}.".format(name = game_data.data[1]["name"], desc = game_data.data[1]["description"], state = game_data.data[1]["country"] ))
# print(type(game_data.data[1]["follower_count"]))