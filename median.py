filename = input("Please enter the filename:" )
f = open(filename, 'r')

numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))
print(numbers)

numbers.sort()
midpoint = len(numbers) // 2
print("The median is ", end = " ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)