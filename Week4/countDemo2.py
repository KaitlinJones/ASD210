from breezypythongui import EasyFrame
import random

class counterDemo(EasyFrame):
        
    def __init__(self):
        EasyFrame.__init__(self, title = "Guessing Game!")
        self.setSize(300, 300)
        self.count = 0 
        self.myNumber = random.randint(1, 100)
        guess = "Is the number " + str(self.myNumber) + "?"
        self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)

        self.addButton(text = "Too Large", row = 1, column = 0, command = self.tooLarge)
        self.addButton(text = "Too Small", row = 1, column = 1, command = self.tooSmall)
        self.addButton(text = "Correct", row = 1, column = 2, command = self.correct)
        self.addButton(text = "New game", row = 1, column = 3, command = self.reset)

    def tooLarge(self):
        self.count += 1
        self.myNumber = random.randint(0, self.myNumber)
        guess = "Is the number " + str(self.myNumber)
        self.label["text"] = guess

    def tooSmall(self):
        self.count += 1
        self.myNumber = random.randint(self.myNumber, 100)
        guess = "Is the number " + str(self.myNumber)
        self.label["text"] = guess
    
    def correct(self):
        self.label["text"] = "It only took me " + str(self.count) + " tries!"
    
    def reset(self):
        self.count = 0
        self.myNumber = random.randint(1, 100)
        guess = "Is the number " + str(self.myNumber) + "?"
        self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)

def main():
    counterDemo().mainloop()

if __name__== "__main__":
    main()