from images import Image
image = Image("smokey.gif")
image.draw()
newImage = image.clone()
newImage.draw()

def main():
    image.draw()
    newImage.draw()

if __name__=="__main__":
    main()