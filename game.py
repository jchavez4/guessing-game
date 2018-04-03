"""A number-guessing game."""

# Put your code here

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player

from random import randint


name = raw_input("Hello,what's your name?")
print "Welcome to the guessing game, %s." % (name)
guess = int(raw_input("I'm thinking of a number between 1 and 100. Can you guess what it is?"))

num_of_guesses = 0

num = randint(1,100)

while guess != num:
    if guess < num:
        guess = int(raw_input("Your guess is too low, try again."))
        num_of_guesses += 1
    elif guess > num:
        guess = int(raw_input("Your guess is too high, try again."))
        num_of_guesses += 1
    
print "Well done, %s! You found my number in %s tries." % (name, num_of_guesses)