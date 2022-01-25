
from breezypythongui import EasyFrame
import random


class counterDemo(EasyFrame):
        
    def __init__(self):
        EasyFrame.__init__(self, title = "Guessing Game!")
        self.count = 1
        self.lowerbound = 1
        self.upperbound = 100
        self.compNum = random.randint(1, 100)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)
       
        self.smallBtn = self.addButton(text = "Too Small", row = 1, column = 0, command = self.tooSmall)
        self.largeBtn = self.addButton(text = "Too Large", row = 1, column = 2, command = self.tooLarge)
        self.correctBtn = self.addButton(text = "Correct", row = 2, column = 0, command = self.correct)
        self.newBtn = self.addButton(text = "New game", row = 2, column = 2, command = self.reset)

    def tooLarge(self):
        # go smaller 
        self.count += 1
        self.upperbound = self.compNum - 1
        self.compNum = (self.upperbound + self.lowerbound) // 2
        guess = "Is the number " + str(self.compNum) + "?"
        self.label["text"] = guess

    def tooSmall(self):
        # go larger 
        self.count += 1
        self.lowerbound = self.compNum + 1
        self.compNum = (self.upperbound + self.lowerbound) // 2
        guess = "Is the number " + str(self.compNum) + "?"
        self.label["text"] = guess
    
    def correct(self):
        self.label["text"] = "It only took me " + str(self.count) + " tries!"
        self.smallBtn["state"] = "disabled"
        self.largeBtn["state"] = "disabled"
        self.correctBtn["state"] = "disabled"
    
    def reset(self):
       self.count = 1
       self.lowerbound = 1
       self.upperbound = 100
       self.compNum = random.randint(1, 100)
       guess = "Is the number " + str(self.compNum) + "?"
       self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)
       self.smallBtn["state"] = "normal"
       self.largeBtn["state"] = "normal"
       self.correctBtn["state"] = "normal"

def main():
    counterDemo().mainloop()

if __name__== "__main__":
    main()
    