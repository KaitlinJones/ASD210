from breezypythongui import EasyFrame
from tkinter import *

class buttonDemo(EasyFrame):
    """Illustrartes command buttons and user events"""
    def __init__(self):
        EasyFrame.__init__(self)

        self.label = self.addLabel(text = "Hello World!", row = 0, column = 0, columnspan = 2, sticky = "NSEW")

        self.clearBtn = self.addButton(text = "Clear", row = 1, column = 0)

        self.restoreBtn = self.addButton(text = "Restore", row = 1, column = 1, state = "disabled")

def main():
    buttonDemo().mainloop()

if __name__=="__main__":
    main()