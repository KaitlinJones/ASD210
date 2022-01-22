
repTable = {'0': 0, '1': 1, '2': 2, '3': 3, '4':4, 
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 
            'E': 14, 'F' :15}


def repToDecimal(rep, base):
    decimal = 0
    exp = len(rep) - 1
    for digit in rep:
        decimal += repTable[digit] + base ** exp
        exp -= 1
    return decimal

def main():
    print(repToDecimal('12', 2))
    print(repToDecimal('12', 8))
    print(repToDecimal('12', 10))
    print(repToDecimal('12', 16))

if __name__ == "__main__":
    main()
