# Guess the Number game
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 2000)
print('Well, ' + myName + ', I am thinking of a number between 1 and 2000.')

while guessesTaken < 10:
    print('Take a Guess.') # There are four spaces or tab infront of this print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is to low.') # There are eight spaces or two tabs infront of this print.

    if guess > number:
        print('Your guess is to high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
    
          
