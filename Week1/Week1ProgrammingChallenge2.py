"""
Kaitlin Jones
ASD 210 - Nathan Kilgore
Week 1 & 2 Programming Challenge

Generate 5 random numbers integer (whole) and store them in 5 separate variables.
Display some instructions to user, on what is expected – i.e. This is a digital lottery for 5 numbers ranging from 1 to 99. You have a chance to win it is you guess all 5 numbers correctly.
Store loop number, i.e. you will need to know if that was 1st loop or 2nd.. etc. 5th.
Start most outer loop. Check what loop number is running.  Use SWIRCH CASE control to  assign maxGuesses variable a corresponding value from those you  generated in the step 1
Start the INNER LOOP – same as given in the BASE CODE, but limit it to 10 attempts.
If user gussed the number correctly during the INNER LOOP execution – REMEMBER the WINNING NUMBER, then  move to NEXT OUTER LOOP CYCLE
IF user exhausted all 10 attempts and did not guess the number correctly - REMEMBER the ZERO,  then  move to NEXT OUTER LOOP CYCLE.
When all cycles completed – you should have your WINNING numbers verified and ready to print."""


import random

maxGuesses = 10
count = 0       # outer loop
count2 = 0      # inner loop
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)
e = random.randint(1, 100)
winningNums = [a, b, c, d, e]
userGuesses1 = []
userGuesses2 = []
userGuesses3 = []
userGuesses4 = []
userGuesses5 = []
print("\nWelcome to the lucky lotto! You will have 10 chances per number to guess 5 random numbers from 1 - 99. If you guess all 5 numbers correctly you win! Miss any of the 5 and you lose. Best of luck to you!\n\n")

print(winningNums) # printing only for testing

for count in range (5):
    count += 1
    userNum = int(input("Please enter your guess for lotto number " + str(count) + ": "))
    for count2 in range(10):
        count2 += 1
        if count == 1:
            if userNum == a:
                print("YOU HIT THE FIRST NUMBER!")
                userGuesses1.append(userNum)
                break
            elif count2 == maxGuesses:
                break
            else: 
                userNum = int(input("Take another guess: "))
                userGuesses1.append(userNum)
        if count == 2:
            if userNum == b:
                print("YOU HIT THE SECOND NUMBER!")
                userGuesses2.append(userNum)
                break
            elif count2 == maxGuesses:
                break
            else: 
                userNum = int(input("Take another guess: "))
                userGuesses2.append(userNum)
        if count == 3:
            if userNum == c:
                print("YOU HIT THE THIRD NUMBER!")
                userGuesses3.append(userNum)
                break
            elif count2 == maxGuesses:
                break
            else: 
                userNum = int(input("Take another guess: "))
                userGuesses3.append(userNum)
        if count == 4:
            if userNum == d:
                print("YOU HIT THE FOURTH NUMBER!")
                userGuesses4.append(userNum)
                break
            elif count2 == maxGuesses:
                break
            else: 
                userNum = int(input("Take another guess: "))
                userGuesses4.append(userNum)
        if count == 5:
            if userNum == e:
                print("YOU HIT THE FIFTH NUMBER!")
                userGuesses5.append(userNum)
                break
            elif count2 == maxGuesses:
                break
            else: 
              userNum = int(input("Take another guess: "))
              userGuesses5.append(userNum)

print("\nThe winning numbers are:", winningNums)
print("\nYour guesses for lotto number 1 were:",userGuesses1)
print("Your guesses for lotto number 2 were:", userGuesses2)
print("Your guesses for lotto number 3 were:", userGuesses3)
print("Your guesses for lotto number 4 were:", userGuesses4)
print("Your guesses for lotto number 5 were:", userGuesses5)