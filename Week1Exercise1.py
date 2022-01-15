"""
Program: sevens.py
Project 3.11
Simulate the game of lucky sevens until all funds are depleted.
1) Rules:
       roll two dice
       if the sum equals 7, win $4, else lose $1
2) The input is:
       the amount of money the user is prepared to lose 
3) Computations:
       use a random number generator to simulate rolling the dice
       loop until the funds are depleted 
       count the number of rolls
       keep track of the maximum amount
4) The outputs are:
       the number of rolls it takes to deplete the funds
       the maximum amount 
"""
import random
# Request the input
dollars = int(input("How many dollars do you have? "))
# Initialize variables
maxDollars = dollars
countAtMax = 0
count = 0
countWins = 0
countLosses = 0 
# Loop until the money is gone
while dollars > 0:
    count += 1
    # Roll the dice
    die1 = random.randint(1, 6)  # 1-6 
    die2 = random.randint(1, 6)  # 1-6
    #Calculate the winnings or losses
    if die1 + die2 == 7:
        dollars += 4
        countWins += 1
    else: 
        dollars -= 1 
        countLosses += 1 
    #If this is a new maximum, remember it
    if dollars > maxDollars:
        maxDollars = dollars
        countAtMax = count
# Display the results
if count == 1:
    print("You are broke after 1 roll.")
else: 
    print("You are broke after " + str(count) + " rolls.")
print("You should have quit after " + str(countAtMax) + \
      " rolls when you had $" + str(maxDollars) + ".")
# Display number of wins and losses 
if countWins == 1:
    print("You won 1 time.")
else: 
    print("You won " + str(countWins) + " times.")
if countLosses == 1: 
    print("You lost 1 time.")
else: 
    print("You lost " + str(countLosses) + " times.")