"""
code = ""
plaintext = input ("enter a message:" )
distance = int(input( "Enter the distance value: "))

for ch in plaintext:
    ordvalue - ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue 

code += distance




bits = input("enter a string of bits: ")

if len (bits) > 1:
    bits = bits[1:] + bits [0]

print(bits)

bitsRight = bits [-1] + bits[:-1]
print(bitsRight)
"""


# INPUT

inname = input("ENTER THE INPUT FILE NAME: ")
outname = input("ENTER THE OUTPUT FILE NAME: ")

# OPEN FILE
inputfile = open(inname, 'r') #reading from the file
text = inputfile.read()

# OUTPUT TO NEW FILE

outfile = open(outname, 'w') # witting file 'w'
outfile.write(text)
outfile.close()
inputfile.close()
