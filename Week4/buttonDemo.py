from breezypythongui import EasyFrame
from tkinter import *

class buttonDemo(EasyFrame):
    """Illustrartes command buttons and user events"""
    def __init__(self):
        EasyFrame.__init__(self)
        self.label = self.addLabel(text = "Hello World!", row = 0, column = 0, columnspan = 4, sticky = "NSEW", foreground = "blue")
        self.clearBtn = self.addButton(text = "Clear", row = 1, column = 0, command = self.clear)
        self.restoreBtn = self.addButton(text = "Restore", row = 1, column = 1, state = "disabled", command = self.restore)
        self.changeColorBtn = self.addButton(text = "Change color", row = 1, column = 2, state = "normal",command = self.changeColor)

    def clear(self):
        """Resets the label to an empty string and the the button states"""
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"
        self.label.config(background="white")
        
    def restore(self):
        """Resets the label to 'Hello World' and sets the state of the butons"""
        self.label["text"]= "Hello World!"
        self.clearBtn["state"] = "normal"
        self.restoreBtn["state"] = "disabled"
        self.label.config(background="white", foreground = "blue")
       
    def changeColor(self):
       self.label.config(background = "green", foreground= "yellow")
       self.restoreBtn["state"] = "normal"

def main():
    buttonDemo().mainloop()

if __name__=="__main__":
    main()