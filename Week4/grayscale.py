"""
File: graysacle.py
Project 7.6
Compares two different grayscale methods.
"""
from images import Image
def grayscale1(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def grayscale2(image):
    """Converts an image to grayscale using the crude average
    of the r, g, and b"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            ave = (r + g + b) // 3
            image.setPixel(x, y, (ave, ave, ave))


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale1(image)
    image.draw()
    newImage = image.clone()                    #clone image to apply grayscale2()
    grayscale2(newImage)
    newImage.draw()
    
    choice = input("Would you like to open a new file? Enter 'y' for yes or press 'q' to exit: ")  # loop to allow for opening 
    if choice != 'q':                                                                              # another file or exiting the 
        main()                                                                                     # program
   
if __name__ == "__main__":
   main()