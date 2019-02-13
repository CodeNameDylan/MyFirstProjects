'''
Created on Feb 12, 2019
This program is for adding 1 to a number depending on its length
@author: Dylan
'''

digit = input("Enter a number between 1 and 1000 to see 1 added to each digit:")
digit = int(digit)
if digit < 10:
    print("Digit Adder outputs: ", digit+1)
elif digit >=10 and digit <100:
    print("Digit Adder outputs: ", digit+11)
elif digit <1000:
    print("Digit Adder outputs: ", digit+111)