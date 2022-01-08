"""
Week 1 Part 2 Hands On
Kaitlin Jones
1/7/22
"""

# Page 62 project 6

mass = float(input("Please enter the object's mass in kilograms: "))
velocity = float(input("Please enter the object's velocity in meters per second: "))
momentum = mass * velocity
keneticEnergy = 0.5 * mass * velocity ** 2 
print("The object has a momentum of ", momentum, "kg.m/s and ", keneticEnergy, "joules of energy.")

