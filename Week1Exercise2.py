"""
Kaitlin Jones 
Program: sum.py
Project 3.9
Computes the sum and average of a series of input numbers.
"""
theSum = 0
count = 0
while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    if float(number) % 2 == 0: # add a condition using modulo that adds only even numbers
        theSum += float(number)
        count += 1
        
print("The sum is", theSum)
if count > 0:
    print("The average is", theSum / count)