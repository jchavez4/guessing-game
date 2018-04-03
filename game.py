"""A number-guessing game."""

from random import randint
num = randint(1, 100)
num_of_guesses = 0

name = raw_input("Hello,what's your name? ")
print "Welcome to the guessing game, %s." % (name)


while True:
    num_of_guesses += 1
    try:
        guess = int(raw_input("I'm thinking of a number between 1 and 100. Can you guess what it is? "))
        break
    except ValueError:
        print "Do you know what a number is?! Try again."


while guess != num:
    if guess < 1 or guess > 100:
        print "You guessed out of range! Please choose a number between 1 and 100. "
    elif guess < num:
        print "Your guess is too low, try again. "
    elif guess > num:
        print "Your guess is too high, try again. "

    while True:
        num_of_guesses += 1
        try:
            guess = int(raw_input("Your guess?"))
            break
        except ValueError:
            print "Do you know what a number is?! Try again."

print "Well done, %s! You found my number in %s tries." % (name, num_of_guesses)