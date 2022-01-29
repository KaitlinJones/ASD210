from breezypythongui import EasyFrame
import tkinter.filedialog
class TextEditor(EasyFrame):
    pass

    def __init__(self):
       EasyFrame.__init__(self, title = "Text Editor")
       self.outputArea = self.addTextArea("", row = 0, column = 0, columnspan = 3, width = 80, height = 15)
       self.addButton(text = "New", row = 1, column = 0, command = self.newFile)
       self.addButton(text = "Open", row = 1, column = 1, command = self.openFile)
       self.addButton(text = "Save", row = 1, column = 2, command = self.saveFile)

    def newFile(self):
        """Clears text field and title bar"""
        self.outputArea.setText = ("")
        self.setTitle("Text Editor")

    def openFile(self):
        """pops open a file dialog displays selected file in the text area"""
        fList = [("Python files", "*.py"), ("Text files", "*.txt"), ("All Files", "*.*")]
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
        if fileName !="":
            file = open(fileName, 'r')
            text = file.read
            file.close
            self.outputArea.setText (text)
            self.setTitle(fileName)

    def saveFile(self):
        fList = [("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")]
        fileName = tkinter.filedialog.asksaveasfilename(parent = self, filetypes = fList)

        if fileName != "":
            file = open(fileName, 'w')
            file.write (self.outputArea.gettext())
            file.close()
            self.setTitle(fileName)


def main():
    TextEditor().mainloop()

if __name__=="__main__":
    main()
