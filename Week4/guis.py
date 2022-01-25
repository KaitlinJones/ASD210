from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    """Disdplays a greeting in a window"""
    def __init__(self):
        """Sets up window and the label"""
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
        self.addLabel(text = "(1, 0 and 1)", row = 1, column = 0, sticky = "NSEW", columnspan = 2)
        #self.addLabel(text = "(1, 1)", row = 1, column = 1, sticky = "NSEW")

def main():
        """Instanciates and pops up the window"""
        LabelDemo().mainloop()

if __name__=="__main__":
        main()
