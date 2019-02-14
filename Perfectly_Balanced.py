'''
Created on Feb 12, 2019

@author: Dylan
This program takes inputs of "x" and "y", counts them and determines if there is an equal amount of each of them
'''

x = 0
y = 0
z = 0
LettersInString = str(input("Enter some Xs and Ys"))

for i in LettersInString:
    if i =="x":
        x += 1
    elif i =="y":
        y += 1
    else:
        z = 1

def balanced(x,y):
    return x - y

if z == 1:
    print("Your input string is invalid. Please use only Xs or Ys.")
elif balanced(x,y) == 0:
    print("Your input string \"" + str(LettersInString) + "\" is balanced!")
elif balanced(x,y) != 0:
    print("Your input string \"" + str(LettersInString) + "\" is not balanced.")
