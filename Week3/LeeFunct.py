def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])

printAll(list(range(11)))
printAll(range(5, 10))
printAll([2,4,6,8,10])

# the function works as expected. The only cost that I could forsee in running this is that it is not possible to format the output?