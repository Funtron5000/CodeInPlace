
from simpleimage import SimpleImage
import random

PUZZLE_IMAGE = SimpleImage('Final/images/slide_shiba_medium.png')
SLIDE_COLUMNS = 3
SLIDE_ROWS = 3
PIECE_WIDTH = PUZZLE_IMAGE.width // SLIDE_COLUMNS
PIECE_HEIGHT = PUZZLE_IMAGE.height // SLIDE_ROWS
SHUFFLES = 6

def main():
    pieces = make_pieces()
    pieces = remove_piece(pieces)
    solved_puzzle = get_puzzle_state(pieces)
    game_loop(solved_puzzle, pieces)

    """
    |1 2 3| This is the solved puzzle
    |4 5 6|
    |7 8 9|

    |1 2 3| Puzzle after removing a piece
    |4 5 0|
    |7 8 9|

    |4 8 2| Shuffled puzzle
    |5 9 1| Here, the user can move 1 or 7 into 0's position
    |3 7 0|

    |1 2 3| But the user will be given this
    |4 5 6|
    |7 8 0|
    """

#sets up the shuffled puzzle and prompts the user for a piece to move
#loops until the state of the user's puzzle matches that of the solved puzzle
def game_loop(solved_puzzle: list, pieces: list):
    pieces = get_shuffled_pieces(pieces)
    current_puzzle = get_puzzle_state(pieces)
    user_puzzle = get_user_state(current_puzzle)
    while current_puzzle != solved_puzzle:
        show_puzzle(pieces)
        move = get_user_move(user_puzzle)
        pieces = move_piece(pieces, move)
        current_puzzle = get_puzzle_state(pieces)
        user_puzzle = get_user_state(current_puzzle)
    PUZZLE_IMAGE.show()
    print('You Win!')

#prompts the user with the current state of the puzzle and asks for which piece to move
def get_user_move(user_puzzle: list)->int:
    valid_moves = get_valid_moves(user_puzzle)
    print('The puzzle is:')
    show_puzzle_state(user_puzzle)
    move = int(0)
    while move not in valid_moves:
        str_move = input(f'Valid moves are: {valid_moves}. Select the piece to move: ')
        if str_move.isnumeric():
            move = int(str_move)
    return move

#swaps the positions of the blank piece and the selected piece
def move_piece(pieces: list, move: int)->list:
    move_index = move - 1
    move_piece = pieces[move_index]

    blank_index = 0
    for piece in pieces:
        if piece[3] == 0:
            blank_piece = piece
            temp_blank_piece = piece.copy()
            blank_row = blank_piece[1]
            blank_column = blank_piece[2]
            break
        blank_index += 1
    
    blank_piece[1], blank_piece[2] = move_piece[1], move_piece[2]
    move_piece[1], move_piece[2] = temp_blank_piece[1], temp_blank_piece[2]

    pieces[blank_index] = move_piece
    pieces[move_index] = blank_piece

    return pieces


#Makes a list of pieces
#These pieces contain the piece image to be moved around
#and the location of that pieces in column, row format as
#piece[1] and piece[2], respectively
#see: make_new_piece function
def make_pieces()->list:
    pieces = []
    position = 1
    for row in range(SLIDE_ROWS):
        for column in range(SLIDE_COLUMNS):
            pieces.append(make_new_piece(column, row, position))
            position += 1
    return pieces

#creates a 'piece' which contains the image, row, column, and position
def make_new_piece(column: int, row: int, position: int)->list:
    x_start = column * PIECE_WIDTH
    y_start = row * PIECE_HEIGHT
    new_image = SimpleImage.blank(PIECE_WIDTH, PIECE_HEIGHT)
    piece_y = 0
    for y in range(y_start, y_start + PIECE_HEIGHT):
        piece_x = 0
        for x in range(x_start, x_start + PIECE_WIDTH):
            new_image.set_pixel(piece_x, piece_y, PUZZLE_IMAGE.get_pixel(x, y))
            piece_x += 1
        piece_y += 1
    #new_image = make_piece_border(new_image)
    return [new_image, column, row, position]

#makes a border around the piece, optional
def make_piece_border(image: SimpleImage)->list:
    border_size = 1
    for pixel in image:
        if (pixel.x <= border_size or pixel.y <= border_size) or (pixel.x >= (image.width - border_size - 1) or pixel.y >= (image.height - border_size - 1)):
            pixel.red = 100
            pixel.green = 100
            pixel.blue = 100
    return image

#removes a piece from the image to make the blank piece
def remove_piece(pieces: list)->list:
    blank_image = SimpleImage.blank(PIECE_WIDTH, PIECE_HEIGHT)
    removed_piece_position = random.randint(1,9)
    new_pieces = []
    for index, list in enumerate(pieces):
        if list[3] == removed_piece_position:
            blank_piece = [blank_image, list[1], list[2], 0]
            new_pieces.append(blank_piece)
        else:
            new_pieces.append(list)
    return new_pieces

#shuffles the pieces by selecting a valid move for the number
#of times set in the SHUFFLES global
def get_shuffled_pieces(pieces: list)->list:
    for n in range(SHUFFLES):
        puzzle = get_puzzle_state(pieces)
        valid_moves = get_valid_moves(puzzle)
        move = random.choice(valid_moves)
        pieces = move_piece(pieces, move)
    return pieces

#shows the current state of the puzzle image
def show_puzzle(pieces: list)->None:
    puzzle = copy_image(PUZZLE_IMAGE)
    for piece in pieces:
        puzzle = place_piece(piece[0], puzzle, piece[1] * PIECE_WIDTH, piece[2] * PIECE_HEIGHT)
    puzzle.show()

#places a piece in the image and returns that image
def place_piece(piece: SimpleImage, working_image: SimpleImage, x_start: int, y_start: int)->SimpleImage:
    piece_y = 0
    for y in range(y_start, y_start + PIECE_WIDTH):
        piece_x = 0
        for x in range(x_start, x_start + PIECE_HEIGHT):
            working_image.set_pixel(x, y, piece.get_pixel(piece_x, piece_y))
            piece_x += 1
        piece_y += 1
    return working_image

#creates a copy of an image so the original is not modified
#necessary for the show_puzzle function so the original image can be presented
def copy_image(image: SimpleImage)->SimpleImage:
    copied_image = SimpleImage.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            copied_image.set_pixel(x, y, pixel)
    return copied_image

#gets a list that represents the state of the puzzle
#where the numbers represent the correct location
def get_puzzle_state(pieces: list)->list:
    puzzle_state = []
    for row in range(SLIDE_ROWS):
        position = row * SLIDE_ROWS
        row_pieces = [pieces[position][3], pieces[position + 1][3], pieces[position + 2][3]]
        puzzle_state.append(row_pieces)
    return puzzle_state

#gets a list that represents the state of the puzzle
#for the user
#numbers are in order with 0 being the blank
#and replacing whichever number should have been there in order
def get_user_state(puzzle_state: list)->list:
    user_state = []
    n = 0
    for row in range(SLIDE_ROWS):
        user_row = []
        for column in range(SLIDE_COLUMNS):
            n += 1
            if puzzle_state[row][column] != 0:
                user_row.append(n)
            else: user_row.append(0)
        user_state.append(user_row)
    return user_state

#shows the state of the puzzle in this form:
# |1 2 3|
# |4 5 6|
# |7 8 0|
#looks much better than printing the list outright
def show_puzzle_state(state: list)->None:
    for i in range(len(state)):
        print(f'|{state[i][0]} {state[i][1]} {state[i][2]}|')

#returns a list of pieces that can be moved
def get_valid_moves(state: list)->list:
    valid_moves = []
    for row in range(SLIDE_ROWS):
        for column in range(SLIDE_COLUMNS):
            if state[row][column] == 0: break
        if state[row][column] == 0: break

    if column == 0 or column == 2:
        valid_moves.append(state[row][1])
    else:
        valid_moves.append(state[row][0])
        valid_moves.append(state[row][2])
    
    if row == 0 or row == 2:
        valid_moves.append(state[1][column])
    else:
        valid_moves.append(state[0][column])
        valid_moves.append(state[2][column])
    valid_moves.sort()
    return valid_moves

if __name__ == '__main__':
    main()