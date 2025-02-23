import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
isContinue = True


while isContinue == True:
    print(art.logo)

    myHand = []
    dealersHand = []

    yn = (input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")).lower()
    if yn == "y":
        print("\n" * 50)
        print(art.logo)
        myHand.append(random.choice(cards))
        myHand.append(random.choice(cards))
        print("\t Your cards: {listCard}, current score: {sumList}".format(listCard =myHand, sumList = sum(myHand)) )

        dealersHand.append(random.choice(cards))

        while sum(dealersHand) <= 21:
            hitDealer = random.choice([True, False])
            if hitDealer == True:
                randomCard = random.choice(cards)
                if randomCard == 11:
                    if randomCard + sum(dealersHand) > 21:
                        randomCard = 1
                dealersHand.append(randomCard)
            elif hitDealer == False:
                break

        print("\t Computer's first card: {firstCard}".format(firstCard=dealersHand[0]))

        while sum(myHand) <= 21:
            hitMe = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
            if hitMe == 'y':
                randomCard = random.choice(cards)
                if randomCard == 11:
                    if randomCard + sum(dealersHand) > 21:
                        randomCard = 1
                myHand.append(randomCard)
                print("\t Your cards: {listCard}, current score: {sumList}".format(listCard=myHand, sumList=sum(myHand)))
                print("\t Computer's first card: {firstCard}".format(firstCard=dealersHand[0]))
                if sum(myHand) > 21:
                    print("   Your final hand: {listCard}, final score: {sumList}".format(listCard = myHand, sumList= sum(myHand)))
                    print("   Computer's final hand: {listCard}, final score: {sumList}".format(listCard=dealersHand, sumList=sum(dealersHand)))
            elif hitMe == 'n':
                print("   Your final hand: {listCard}, final score: {sumList}".format(listCard = myHand, sumList= sum(myHand)))
                print("   Computer's final hand: {listCard}, final score: {sumList}".format(listCard=dealersHand, sumList=sum(dealersHand)))
                break

        if sum(myHand) == sum(dealersHand):
            print("Draw")
        elif sum(myHand) > 21:
            print("You went over. You lose")
        elif sum(dealersHand) > 21:
            print("Opponent went over. You win")
        elif sum(myHand) > sum(dealersHand):
            print("You win")
        elif sum(myHand) < sum(dealersHand):
            print("You lose")



    elif yn == "n":
        isContinue = False

    else:
        isContinue = False
