from random import randint

class Die:
    """This class represents a six sided die"""

    def __init__(self):
        """Creates a new die with a value of one."""
        self.value = 1
    
    def roll(self):
        """Resets the die's value to a random int between 1 and 6"""
        self.value = randint(1, 6)

    def getValue(self):
        return self.value

    def __str__(self):
        """Returns the string rep of the Die"""
        return str(self.value())

def main():
    return

if __name__ == "__main__":
    main()