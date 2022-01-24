from images import Image

def posterize(image, color):
    """converts an image to white and a user specified RGB value or a default value of black"""
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) //3
            if average < 128:
                image.setPixel(x, y, color)
            else:
                image.setPixel (x, y, whitePixel)

def main():
    filename = input("Enter the image filename:")
    red = input("Enter a value for red between 0-255:")
    green = input("Enter a value for green between 0-255:")
    blue = input("Enter a value for blue between 0-255:")
    rgbTup = (int(red), int(green), int(blue))
    image = Image(filename)
    posterize(image, rgbTup)
    image.draw()

    if __name__=="__main__":
        main()
