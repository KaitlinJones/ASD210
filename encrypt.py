"""
ASD 210 Fundamentals of Python and Best Practices - Nathan Kilgore
Kaitlin Jones
Week 2 Hands On 1
Jan 15 2021
"""

plainText = str(input("\nPlease enter a message: "))
distance = int(input("Please enter the distance: "))

for i in range(len(plainText)):
    print(chr((ord(plainText[i]) + distance)), end = "")
print("\n")
    