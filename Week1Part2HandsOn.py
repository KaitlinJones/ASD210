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


