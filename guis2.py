
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Displays captions"""

    def __init__(self):
        EasyFrame.__init__(self, title="ImageDemo")
        self.setResizable(False);
        imageLabel = self.addLabel(text="", row = 0, column = 0, sticky = "NSEW")
        textLabel = self.addLabel (text = "Smokey the Cat", row = 1, column = 0, sticky = "NSEW")

        self.image = PhotoImage(file = "smokey.gif")
        imageLabel["image"] = self.image

        font = Font(family = "Veranda", size = 20, slant = "italic")
        textLabel["font"]= font
        textLabel["foreground"] = "blue"
    
def main():
    ImageDemo().mainloop()

if __name__ == "__main__":
    main()



