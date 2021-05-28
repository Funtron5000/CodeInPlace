
"""
Karel movements in first-person
Constants for the grid and starting position and direction are defind
Global variables are used for Karel's current position and direction
"""

#The world is made of columns and rows
#Starting in the bottom-left location
#which is defined as row 1, column 1
#Indices increase going right and up (east and north)
WORLD_COLUMNS = 5           #Number of columns in the world
WORLD_ROWS = 5              #Number of rows in the world
START_COLUMN = 1            #Starting column
START_ROW = 1               #Starting row
START_DIRECTION = 'east'    #Starting direction

#Prompt for getting an action
ACTION_PROMPT = 'What would you like to do? ' \
    'Type move, turn left, turn right, find edge,\n' \
    'face north, face west, face south, face east, or status.\n' \
    'Giving no response will exit.\n'

#Global variables for tracking Karel's position and direction
Karel_Column = START_COLUMN
Karel_Row = START_ROW
Karel_Direction = START_DIRECTION

#Welcomes the user, gives the status, and runs get_action
def run_karel():
    print('Welcome to first-person Karel!')
    status()
    get_action()

#Continually prompts the user to give an action, exits if no action given
def get_action():
    action = input(ACTION_PROMPT)
    while action != '':
        run_action(action)
        action = input(ACTION_PROMPT)
    print('Good-bye!',end='')

#Runs the given action, if it's invalid, calls bad_command
def run_action(action: str):
    print()
    action = action.lower()
    if action == 'turn left':
        turn_left()
    elif action == 'turn right':
        turn_right()
    elif action == 'move':
        move()
    elif action == 'find edge':
        find_edge()
    elif action == 'status':
        status()
    elif action[:4] == 'face':
        try:
            direction = action.rsplit(' ', 1)[1]
        except:
            bad_command(action)
            return
        face(direction)
    else:
        bad_command(action)

#Makes Karel turn left
def turn_left():
    global Karel_Direction
    if Karel_Direction == 'north':
        Karel_Direction = 'west'
    elif Karel_Direction == 'west':
        Karel_Direction = 'south'
    elif Karel_Direction == 'south':
        Karel_Direction = 'east'
    else:
        Karel_Direction = 'north'
    print(f'Karel turns left!')
    status()

#Makes Karel turn right
def turn_right():
    global Karel_Direction
    if Karel_Direction == 'north':
        Karel_Direction = 'east'
    elif Karel_Direction == 'west':
        Karel_Direction = 'north'
    elif Karel_Direction == 'south':
        Karel_Direction = 'west'
    else:
        Karel_Direction = 'south'
    print(f'Karel turns right!')
    status()

#Moves Karel forward one space in the current direction
def move():
    global Karel_Row
    global Karel_Column
    global Karel_Direction

    if Karel_Direction == 'north' and Karel_Row < WORLD_ROWS:
        Karel_Row += 1
    elif Karel_Direction == 'west' and Karel_Column  > 1:
        Karel_Column -= 1
    elif Karel_Direction == 'south' and Karel_Row > 1:
        Karel_Row -= 1
    elif Karel_Direction == 'east' and Karel_Column < WORLD_COLUMNS:
        Karel_Column += 1
    else:
        print('The front is blocked!')
        return
    print('Karel moves forward!')
    status()

#Karel moves to the edge of the grid in the current direction
def find_edge():
    global Karel_Row
    global Karel_Column
    global Karel_Direction

    if Karel_Direction == 'north':
        Karel_Row = WORLD_ROWS
    elif Karel_Direction == 'west':
        Karel_Column = 1
    elif Karel_Direction == 'south':
        Karel_Row = 1
    elif Karel_Direction == 'east':
        Karel_Column = WORLD_COLUMNS
    
    print(f'Karel moves to the {Karel_Direction} edge!')
    status()

#Turns Karel to face the given direction
def face(direction: str):
    global Karel_Direction

    if direction in ('north', 'west', 'south', 'east'):
        Karel_Direction = direction
        print(f'Karel turns to face {direction}!')
        status()
    else:
        bad_command('face ' + direction)

#Prints the bad action you tried to give
def bad_command(action: str):
    print(f'{action} is not a valid command!')

#Prints the current status of Karel: position and direction
def status():
    global Karel_Row
    global Karel_Column
    global Karel_Direction
    print(f'Karel is at row {Karel_Row}, column {Karel_Column}, and facing {Karel_Direction}.')

if __name__ == "__main__":
    run_karel()