from simpleimage import SimpleImage

BRIGHT_THRESHOLD = 153

def main():
    images = []
    shiba = SimpleImage('week3/images/shiba.png')
    #images.append(shiba)
    #images.append(darken(shiba))
    #images.append(grayscale(shiba))
    #images.append(narok(shiba))
    #images.append(border(shiba, 10))
    #for image in images:
    #    image.show()
    bordered = border(shiba, 10)
    bordered.show()


def copy_image(image: SimpleImage)->SimpleImage:
    copied_image = SimpleImage.blank(image.width, image.height)
    for pixel in image:
        copied_image.set_pixel(pixel.x, pixel.y, pixel)
    return copied_image

def darken(image: SimpleImage)->SimpleImage:
    dark_image = copy_image(image)
    for pixel in dark_image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
    return dark_image

def grayscale(image: SimpleImage)->SimpleImage:
    gray_image = copy_image(image)
    for pixel in gray_image:
        luminence = (0.299 * pixel.red) + (0.587 * pixel.green) + (0.114 * pixel.blue)
        pixel.red = luminence
        pixel.green = luminence
        pixel.blue = luminence
    return gray_image

def narok(image: SimpleImage)->SimpleImage:
    narok_image = copy_image(image)
    for pixel in narok_image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if average > BRIGHT_THRESHOLD:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return narok_image

def border(image: SimpleImage, border_size: int)->SimpleImage:
    border_image = copy_image(image)
    width = border_image.width
    height = border_image.height
    for pixel in border_image:
        if (pixel.x <= border_size or pixel.y <= border_size) or (pixel.x >= (width - border_size) or pixel.y >= (height - border_size)):
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 0
    return border_image

if __name__ == '__main__':
    main()