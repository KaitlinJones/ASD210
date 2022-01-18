octal = input("Please enter an octal number: ")
decimal = 0
exponent = len(octal) - 1
for digit in octal:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent -= 1
print("The integer value is: ", decimal)