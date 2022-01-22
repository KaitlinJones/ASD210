"""write a program that inputs a txt file. The program should output the unique words of the file in alphabetical order."""

in_name = input("Enter the name of the file you want to open: ")

in_file = open(in_name, 'r')
unique_words = []

for line in in_file:
    words = line.split()
    for word in words:
        if not word in unique_words:
            unique_words.append(word)

unique_words.sort()

for word in unique_words:
    print(word)