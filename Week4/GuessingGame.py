from ast import Store
from breezypythongui import EasyFrame
import random

class counterDemo(EasyFrame):
        
    def __init__(self):
        EasyFrame.__init__(self, title = "Guessing Game!")
        self.setSize(300, 300)
        self.count = 1
        self.lowerbound = 1
        self.upperbound = 100
        self.compNum = random.randint(1, 100)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)
        
        self.addButton(text = "Too Small", row = 1, column = 0, command = self.tooSmall)
        self.addButton(text = "Too Large", row = 1, column = 1, command = self.tooLarge)
        self.addButton(text = "Correct", row = 2, column = 0, command = self.correct)
        self.addButton(text = "New game", row = 2, column = 1, command = self.reset)

    def tooLarge(self):
        self.count += 1
        self.lowerbound = self.compNum + 1
        self.compNum = (self.upperbound + self.lowerbound) // 2
        #self.compNum = random.randint(self.lowerbound, self.compNum)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label["text"] = guess

    def tooSmall(self):
        self.count += 1
        self.upperbound = self.compNum - 1
        self.compNum = (self.upperbound + self.lowerbound) // 2
        #self.compNum = random.randint(self.compNum, self.upperbound)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label["text"] = guess
    
    def correct(self):
        self.label["text"] = "It only took me " + str(self.count) + " tries!"
        self.tooLarge["state"] = "disabled"
        self.tooSmall["state"] = "disabled"
        self.correct["state"] = "disabled"
    
    def reset(self):
        self.count = 1
        self.compNum = random.randint(1, 100)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)

def main():
    counterDemo().mainloop()

if __name__== "__main__":
    main()
    