"""
File: average.py
Project 6.9
Prints the average of the numbers in a text file 

Task to Accomplish
The Base Code allows printing average  of  numbers.  You will need to add:

Calculation and printing for Minimum ( the smallest number) and
the maximum ( the biggest number)
Have all print out to be defined as Functions ( you will need 3 functions: one for average, 2nd for Minimum, and the 3rd for Maximum)
How to proceed:
Make sure the Base Code (as offered in this exercise) is running without errors ( note: both Python program and “numbers.txt” file must be located in the same folder, and all data in the “numbers.txt  file must have space as deliminator separating the field in the same line)
Transform block for Average into Python Function,  and design   new code blocks as Functions - for  Maximum and Minimum
Design and PRINT output to display required results
When successful – Take a screenshot of successfully tested program.
"""
from functools import reduce

fileName = input("Enter the input file name: ")
inputFile = open(fileName, 'r')                     # Accept the input file name and open the file

lyst = []
for line in inputFile:
    lyst.extend(line.split())           # Read the numbers as strings into a list

print(lyst) #added 

lyst = list(map(float, lyst))       # Convert all the strings in the list to numbers

summation = reduce(lambda x, y: x + y, lyst)    # Compute the sum of the numbers

maximum = reduce(lambda x, y: x if x > y else y, lyst)         # compute maximum
minimum = reduce(lambda x, y: x if x < y else y, lyst)         # compute minimum 

if len(lyst) == 0:
    average = 0
else:
    average = summation / len(lyst)
print("The average is", average)        # Print the average
print("The minimum is ", minimum)       # Print the minimum
print("The maximum is", maximum)        # Print the maximum