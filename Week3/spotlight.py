"""
Makes a 'spotlight' on an image
pass an image to the spotlight function with the percent of image to spotlight, how much to brighten and darken
and get back an image with a spotlight

Currently there is no fade of light toward the outside of the spotlight, so it makes a harsh edge
This should be able to be calculated as a factor of the distance from the center to the edge of
the radius to spotlight, but I havent' done that yet
"""
from simpleimage import SimpleImage
from math import pi

def main():
    my_image = SimpleImage('week3/images/shiba.png')
    spotlight_image = spotlight(my_image, .9, 1.2, 0.5)
    my_image.show()
    spotlight_image.show()

#Creates a copy of the image that is seperate from the original image
#Allows for filters to be done without modifying the originally passed image
def copy_image(image: SimpleImage)->SimpleImage:
    copied_image = SimpleImage.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            copied_image.set_pixel(x, y, pixel)
    return copied_image

#Gets the image to spotlight and the spotlight parameters
#utilizes copy_image so that the original image is not modified
#uses make_circle to get coordinates to brighten and darken
def spotlight(image: SimpleImage, spotlight_percent: float, brighten: float, darken: float)->SimpleImage:
    spotlight_image = copy_image(image)
    if spotlight_percent > 1.0:
        spotlight_image = 1.0
    width = image.width
    height = image.height
    circle, dark_area = make_circle(width, height, spotlight_percent)
    for bright_coord in circle:
        pixel = spotlight_image.get_pixel(*bright_coord)
        pixel.red *= brighten
        pixel.green *= brighten
        pixel.blue *= brighten
    for dark_coord in dark_area:
        pixel = spotlight_image.get_pixel(*dark_coord)
        pixel.red *= darken
        pixel.green *= darken
        pixel.blue *= darken
    return spotlight_image

#makes the circle to spotlight and the area outside of that circle to darken
#first calculates the radius and then uses the distance function to determine
#if a pixel is between the midpoint and the midpoint + radius
#both bright_circle and dark_area are returned as tuples of (x,y) members
#these are the coordinates in the image to modify
def make_circle(width: int, height: int, percent: float)->tuple(tuple, tuple):
    radius = int(min(width, height) / 2 * percent)
    midpoint = (width//2, height//2)
    bright_circle = []
    dark_area = []
    for y in range(height):
        for x in range(width):
            if distance(x, y, *midpoint) <= radius:
                bright_circle.append((x, y))
            else:
                dark_area.append((x, y))
    return tuple(bright_circle), tuple(dark_area)

#cartessian coordinate distance calculation for 2D returned as an integer
def distance(x1: int, y1: int, x2: int, y2: int)->int:
    return int(((x2-x1)**2 + (y2-y1)**2)**0.5)


if __name__ == '__main__':
    main()