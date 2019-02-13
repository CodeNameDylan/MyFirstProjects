'''
Created on Feb 12, 2019

@author: Dylan
'''
from random import randint
reroll = True
while reroll:
    print("The number rolled on the dice was a",randint(1,6))
    print("Would you like to roll again?")
    reroll = ("y" or "yes") in input().lower()
else:
    print("Thank you for playing!")