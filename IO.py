'''
Created on Feb 13, 2019

@author: Dylan
This program takes multiple user inputs as a number, saves fart energy and outputs the nmbers entered, the sum of numbers,the highest and lowest entered, and the mean
'''
from sre_compile import isstring
import statistics
answered_int = True
integersList = []
while answered_int == True:
    answer = input("Enter a number or Enter to finish: ")
    try:
        answer_int = int(answer)
        integersList.append(int(answer_int))
    except ValueError:
        if isstring(answer_int):
                print("An error has occured. Please try again")
    if answer == "":
            equations = input("Press 1 to see the various outputs of this program, 2 to quit: ")
            if int(equations) == 1:
                print("Sum of entered numbers is: ", sum(integersList))
                print("Highest Number: ", max(integersList) , "Lowest Number: ", min(integersList) )
                print("The average of the input numbers is: ", sum(integersList)/len(integersList))
                print("The median of the input numbers is: ", statistics.median(integersList))
                break
            elif int(equations) == 2:
                print("Thank you for trying my program")
                break
            else:
                print("Please enter a number between 1-100")

