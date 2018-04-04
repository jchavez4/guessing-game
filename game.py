"""A number-guessing game."""

from random import randint
num = randint(1, 100)
num_of_guesses = 0
guess = 0
answer = 'y'
best_score = 1000

name = raw_input("Hello,what's your name? ")
print "Welcome to the guessing game, %s. Guess a number between 1 and 100." % (name)

while guess != num and answer == 'y':
    while True:
        num_of_guesses += 1
        try:
            guess = int(raw_input("Your guess?"))
            break
        except ValueError:
            print "Do you know what a number is?! Try again."
    if guess < 1 or guess > 100:
        print "You guessed out of range! Please choose a number between 1 and 100. "
    elif guess < num:
        print "Your guess is too low, try again. "
    elif guess > num:
        print "Your guess is too high, try again. "
    elif guess == num:
        print "Well done, %s! You found my number in %s tries." % (name, num_of_guesses)
        if num_of_guesses < best_score:
            best_score = num_of_guesses
            print "That's your best score yet!"
        elif num_of_guesses > best_score:
            print "Your current best score is %s tries." % (best_score)
        answer = raw_input("Would you like to play again? y or n? ")
        while answer != 'y' and answer != 'n':
            answer = raw_input("Invalid input. Please enter y or n. ")
        if answer == 'y':
            num = randint(1, 100)
            num_of_guesses = 0
            guess = 0
            print "Guess a number between 1 and 100."

print "Thanks for playing!"
print "Your best score was %s tries!" % (best_score)
