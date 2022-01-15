"""Generate 5 random numbers integer (whole) and store them in 5 separate variables.
Display some instructions to user, on what is expected – i.e. This is a digital lottery for 5 numbers ranging from 1 to 99. You have a chance to win it is you guess all 5 numbers correctly.
Store loop number, i.e. you will need to know if that was 1st loop or 2nd.. etc. 5th.
Start most outer loop. Check what loop number is running.  Use SWIRCH CASE control to  assign maxGuesses variable a corresponding value from those you  generated in the step 1
Start the INNER LOOP – same as given in the BASE CODE, but limit it to 10 attempts.
If user gussed the number correctly during the INNER LOOP execution – REMEMBER the WINNING NUMBER, then  move to NEXT OUTER LOOP CYCLE
IF user exhausted all 10 attempts and did not guess the number correctly - REMEMBER the ZERO,  then  move to NEXT OUTER LOOP CYCLE.
When all cycles completed – you should have your WINNING numbers verified and ready to print."""


import random

print("Welcome to the lucky lotto! You will have 10 chances per number to guess 5 random numbers from 1 - 99. If you guess all 5 numbers correctly you win! Miss any of the 5 and you lose. Best of luck to you!")
x = 0
maxGuesses = 10
count = 0
count2 = 0 
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)
e = random.randint(1, 100)
winningNums = [a, b, c, d, e]
userGuess = []
print(winningNums)

for count in range (5):
    count += 1
    userNum = int(input("Please enter your guess for lotto number " + str(count) + ":"))
    for count2 in range(10):
        count2 += 1
        if userNum == winningNums[0]:
            print("YOU HIT THE FIRST NUMBER!")
            break
        elif userNum == winningNums[1]:
            print("YOU HIT THE SECOND NUMBER:")
            break
        else: 
            userNum = int(input("Take another guess:"))
        

#if x == a:
    pass

"""
count = 0
while i <= 10:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small")
    elif userNumber > myNumber:
        print("Too large")
    else:
        print("You've got it in", count, "tries!")
        break
"""

print("The winning numbers are:", winningNums)