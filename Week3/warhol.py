"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'Week3/images/shiba.png'
PINK_FILTER = (1.5, .5, 1.5)
GREEN_FILTER = (.55, 1.5, 1.3)
BLUE_FILTER = (.55, 1.1, 4.0)
YELLOW_FILTER = (1.7, 1.8, .8)
BRIGHT_FILTER = (1.6, 1.6, 1.6)

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    # This is an example which should generate a pinkish patch
    #patch = make_recolored_patch(1.5, 0, 1.5)
    pink_patch = make_recolored_patch(*PINK_FILTER)
    green_patch = make_recolored_patch(*GREEN_FILTER)
    bright_patch = make_recolored_patch(*BRIGHT_FILTER)
    yellow_patch = make_recolored_patch(*YELLOW_FILTER)
    normal_patch = SimpleImage(PATCH_NAME)
    blue_patch = make_recolored_patch(*BLUE_FILTER)
    patch_tuple = (pink_patch, green_patch, bright_patch, yellow_patch, normal_patch, blue_patch)
    final_image = make_final_image(patch_tuple, final_image)
    final_image.show()

def make_final_image(patches: tuple, final_image: SimpleImage)->SimpleImage:
    current_patch = 0
    for row in range(N_ROWS):
        for column in range(N_COLS):
            final_image = place_patch(patches[current_patch], final_image, column * PATCH_SIZE, row * PATCH_SIZE)
            current_patch += 1
    return final_image

def place_patch(patch: SimpleImage, working_image: SimpleImage, x_start: int, y_start: int)->SimpleImage:
    patch_y = 0
    for y in range(y_start, y_start + PATCH_SIZE):
        patch_x = 0
        for x in range(x_start, x_start + PATCH_SIZE):
            working_image.set_pixel(x, y, patch.get_pixel(patch_x, patch_y))
            patch_x += 1
        patch_y += 1
    return working_image

#def make_new_patch(red_scale, green_scale, blue_scale):
#    patch = SimpleImage(PATCH_NAME)
#    patch = make_gray(patch)
#    for pixel in patch:
#        pixel.red *= red_scale
#        pixel.green *= green_scale
#        pixel.blue *= blue_scale
#    patch.show()

def make_colored(image, color):
    l_red = 0.299
    l_green = 0.587
    l_blue = 0.114
    factor = 2.0

    for pixel in image:
        lumonosity = (0.299 * pixel.red) + (0.587 * pixel.green) + (0.114 * pixel.blue)
        if color == 'red':
            pixel.red = lumonosity * 5
            lumonosity = (0.299 * pixel.red) + (0.587 * pixel.green) + (0.114 * pixel.blue)
            pixel.green = lumonosity
            pixel.blue = lumonosity
        #pixel.red = lumonosity
        #pixel.green = lumonosity
        #pixel.blue = lumonosity
    return image

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    #patch.show()
    return patch


if __name__ == '__main__':
    main()