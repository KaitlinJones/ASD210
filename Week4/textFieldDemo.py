from breezypythongui import EasyFrame
from tkinter import *

class textFieldDemo(EasyFrame):
    """Converts an input string to uppercase and displays the result"""

    def __init__(self):
        """Sets up the window and widgets"""
        EasyFrame.__init__(self, title = "Text Field Window")
        self.addLabel(text = "Input", row = 0, column = 1)
        self.inputField = self.addTextField(text = "Input", row = 0, column = 1)

        self.addLabel(text = "Output", row = 1, column = 0)
        self.outputField = self.addTextField(text= "", row = 1, column = 1, state = "readonly")

        self.addButton(text = "Convert", row = 2, column = 0, columnspan = 2, command = self.convert)

    def convert(self):
        """Imputs the string, converts to uppercase, and outputs the result."""
        text = self.inputField.getText()
        result = text.upper()
        self.outputField.setText(result)

def main():
    textFieldDemo().mainloop()

if __name__=="__main__":
    main()