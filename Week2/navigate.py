"""
File: navigate.py
Project 5.2
Allows the user to navigate to any line in a text file.
"""
print("\nProgram to combine strings from a txt file! ")
# Take the input file name
inName = input("Enter the input file name: ")
# Open the input file and read the text
inputFile = open(inName, 'r')
lines = []
for line in inputFile:
    lines.append(line)
    
# Loop for line numbers from the user until she enters 0
while True:
    print("\n*** The file has", len(lines), "lines. ***") # asterisks to denote the start of the program
    if len(lines) == 0:
        break
    lineNumber1 = int(input("\nEnter the first line number [0 to quit]: "))
    if lineNumber1 == 0:
        break
    lineNumber2 = int(input("\nEnter the second line number [0 to quit]:")) # modify loop to take 2nd line
    if lineNumber2 == 0:
        break
    elif lineNumber1 >= len(lines):
        print("ERROR: line number must be less than", len(lines))
    elif lineNumber2 >= len(lines):
        print("ERROR: line number must be less than", len(lines))
    else:
        newList = [lines[lineNumber1] + lines[lineNumber2]] #create new list by concatenating indices
        newString =" ".join(newList) # convert newList to string with join method 
        print("\n",str(newString.replace("\n", " " )))   # replace all instances of \n characters with spaces 
        print("\nThe length of the new string is: ", len(newString))


        