from ast import Store
from breezypythongui import EasyFrame
import random

class counterDemo(EasyFrame):
        
    def __init__(self):
        EasyFrame.__init__(self, title = "Guessing Game!")
        self.setSize(300, 300)
        self.count = 1
        self.lowerbound = 0
        self.upperbound = 0
        self.compNum = random.randint(1, 100)
        self.storeComp = []
        guess = "Is the number " + str(self.compNum) + "?"
        self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)
        for i in self.storeComp:
            self.storeComp.append(self.compNum)

        self.addButton(text = "Too Large", row = 1, column = 0, command = self.tooLarge)
        self.addButton(text = "Too Small", row = 1, column = 1, command = self.tooSmall)
        self.addButton(text = "Correct", row = 2, column = 0, command = self.correct)
        self.addButton(text = "New game", row = 3, column = 1, command = self.reset)

    def tooLarge(self):
        self.upperbound = self.compNum 
        self.lowerbound = min(self.storeComp)
        self.count += 1
        self.compNum = random.randint(0, self.compNum)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label["text"] = guess

    def tooSmall(self):
        self.lowerbound = self.compNum
        self.upperbound = max(self.storeComp)
        self.count += 1
        self.compNum = random.randint(self.compNum, 100)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label["text"] = guess
    
    def correct(self):
        self.label["text"] = "It only took me " + str(self.count) + " tries!"
    
    def reset(self):
        self.count = 1
        self.compNum = random.randint(1, 100)
        guess = "Is the number " + str(self.compNum) + "?"
        self.label = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)

def main():
    counterDemo().mainloop()

if __name__== "__main__":
    main()
    