"""
Week 1 Part 2 Hands On
Kaitlin Jones
1/7/22
"""

# Page 62 project 6

print("Program to calculate an object's momentum and kenetic energy.\n")

mass = float(input("Please enter the object's mass in kilograms: "))
velocity = float(input("Please enter the object's velocity in meters per second: "))

momentum = mass * velocity
keneticEnergy = 0.5 * mass * velocity ** 2 

print("\nThe object has a momentum of ", momentum, "kg.m/s.")
print("The object's kenetic energy calculates to ", keneticEnergy, "joules.")


# Page 63 Project 10

print("\nProgram to calulate and employee's weekly salary: ")

# Take input from user
payRate = float(input("\nPlease enter your hourly pay rate:  "))
hours = float(input("Please enter your regular hours worked:  "))
overTime = float(input("Please enter you ovetime hours worked:  "))

# Caculations 
regPay = hours * payRate 
overTimeRate = 1.5 * payRate
overTimePay = overTimeRate * overTime
totalPay = regPay + overTimePay

# Output
print("\nYour regular pay is: $", round(regPay, 2))
print("\nYour overtime pay is: $", round(overTimePay, 2))
print("\nYour total pay is: $", round(totalPay, 2))


# Page 100 Project 8

# Take input from user
smallNum = int(input("\nPlease enter a number: "))
largeNum = int(input("Please enter a number that is smaller than the first number that you entered: "))

# calculate using Euclid's algorithm
while smallNum > 0:
    remainder = largeNum % smallNum
    largeNum = smallNum
    smallNum = remainder

print("The greatest common denominator is ", largeNum)


# Page 101 Project 9

theSum = 0    #set sum to 0
count = 0     # set count to 0

# Take input from user until enter is pressed

while True:
    number = input("Please enter a number or press 'enter' to quit: ")
    if number == "":
        break
    
# Calculate and print sum

    theSum += float(number)
    count += 1

print("The sum is : ", theSum)

# Calculate and print average
    
if count > 0:
    print("The average is: ", theSum / count)



