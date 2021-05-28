
"""
Trims the edges of an image based on the number of pixels given
"""

from simpleimage import SimpleImage

def main():
    image = SimpleImage('week3/images/shiba.png')
    image.show()
    trimmed = trim_crop(image, 25)
    trimmed.show()

def trim_crop(image: SimpleImage, trim_size: int):
    og_width = image.width
    og_height = image.height
    trimmed_width = og_width - (trim_size * 2)
    trimmed_height = og_height - (trim_size * 2)
    trimmed_image = SimpleImage.blank(trimmed_width, trimmed_height)
    for y in range(trimmed_height):
        for x in range(trimmed_width):
            og_x = trim_size + x
            og_y = trim_size + y
            trimmed_image.set_pixel(x, y, image.get_pixel(og_x, og_y))
    return trimmed_image

if __name__ == '__main__':
    main()