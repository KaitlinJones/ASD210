import random
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Guessing  Game")
        # Initialize the instance variables for the data
        
        self.count = 0
        # Create and add widgets to the window
        greeting = "Enter a number between 1 and 100."
        self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0, sticky = "NSEW", columnspan = 2)
        self.addLabel(text = "Your guess", row = 1, column = 0)
        self.guessField = self.addIntegerField(0, row = 1, column = 1)
        # Buttons have no command attributes yet
        self.largeButton = self.addbutton(text = "Too Large")
        self.smallButton = self.addbutton(text = "Too Small", row = 1, column = 1)
        self.correctButton = self.addButton(text = "Correct", row = 2, column = 0)
        self.newButton = self.addButton(text = "New game", row = 2, column = 1)
def main():
    GuessingGame().mainloop()

if __name__ == "__main__":
    main()

