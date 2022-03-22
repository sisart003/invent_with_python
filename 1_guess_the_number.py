# This is a guess the number game.
import random

guessesTaken = 5
guessAttempt = 0

print("Hello! What is your Name? ")

yourName = input()

number = random.randint(1, 20)

print("Well, " + yourName + ", I am thinking of a number between 1 and 20. ")
print("You have 6 lives")

while guessesTaken > 0:
    
    print("Take a Guess.") # There are four space in front of print

    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken - 1
    guessAttempt = guessAttempt + 1

    if guess < number:
        print("You only have " + str(guessesTaken) + " Lives")
        print("Print guess is too low") # There are eight space in front of print

    if guess > number:
        print("You only have " + str(guessesTaken) + " Lives")
        print("Your guess is too high")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good Job, " + yourName + "! You guessed my number in " + str(guessAttempt) + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number)
    
