from breezypythongui import EasyFrame
from tkinter import *
import math

class numberFieldDemo(EasyFrame):
    
    def __init__(self):
        """Sets up the window and widgets"""
        EasyFrame.__init__(self, title = "Text Field Window")
        
        self.addLabel(text = "An Integer", row = 0, column = 1)
        self.inputField = self.addIntegerField(value = 0, row = 0, column = 0, width = 10)
        
        self.addLabel(text = "Square Root", row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 8, precision = 2, state = "readonly")

        self.addButton(text= "compute!", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)

    def computeSqrt(self):
        try:
            number = self.inputField.getNumber()
            result = math.sqrt(number)
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title = "ERROR", message ="Input must be an integer >= 0!")
            

def main():
    numberFieldDemo().mainloop()

if __name__ == "__main__":
    main()