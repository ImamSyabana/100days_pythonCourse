from random import randint

import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input(str("Choose a difficulty. Type 'easy' or 'hard':"))
if difficulty.lower() == "easy":
    attempt = 10
elif difficulty.lower() == "hard":
    attempt = 5

secretNumber = randint(0,100)

for x in range(attempt):
    print("You have {kesempatan} attempts remaining to guess the number.".format(kesempatan = attempt))
    guessInput = int(input(("Make a guess: ")))
    attempt = attempt - 1
    if guessInput == secretNumber:
        print("You got it! The answer was {num}".format(num = secretNumber))
    elif guessInput < secretNumber:
        print("Too Low.")
        if attempt != 0:
            print("Guess Again")
        else:
            print("Game over. You've run out of guesses. Reload to run again.")
    elif guessInput > secretNumber:
        print("Too High.")
        if attempt != 0:
            print("Guess Again")
        else:
            print("Game over. You've run out of guesses. Reload to run again.")



