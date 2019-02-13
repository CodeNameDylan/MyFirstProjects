'''
Created on Feb 12, 2019

@author: Dylan
'''
import random
guessesTaken = 0
randomNum = random.randint(1,20)
print("Try to guess the number between 1-20 that I am thinking? You have 5 tries")
while guessesTaken <6:
    guess = input()
    guess = int(guess)
    
    guessesTaken = guessesTaken +1
   
    if guess < randomNum:
        print("Guess is too low!")
    elif guess > randomNum:
        print("Guess is too high!")
        guessesTaken = +1
    else:
        print("You guessed it! The number was ",randomNum)
        break
else:
    print("Sorry, the number was ",randomNum,", please try again.")
