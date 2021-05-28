"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'Week3/images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)
    print(image.height)
    reflection = SimpleImage.blank(image.width, image.height * 2)
    print(reflection.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            reflection.set_pixel(x, y, pixel)
            reflection.set_pixel(x, reflection.height - (y + 1) , pixel)
    return reflection


def main():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()