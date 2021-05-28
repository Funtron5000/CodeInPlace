"""
Plays the game, Nimm
A pile of stones exists and each player takes turns removing one or two stones
Whoever is last to take from the pile loses
The number of stones, players, and acceptable removals can be modified if desired by the constants

An 'AI' can be employed to always win
In order to win, the player or AI must end a turn with 4 stones left in the pile
"""

import random
#Keep this number in the form of 3n or 3n + 2 to always have the AI win
#Change this number to a different form to have a chance at winning
INITIAL_STONES = 20
PLAYER_COUNT = 2
ACCEPTABLE_REMOVAL = [1,2]

def main():
    nimm()

def game_over(player: int)->str:
    print(f'Player {player}, you lose.')
    print('Game over')

def remove_stones(pile: int, player: int)->int:
    """
    function for removing stones
    will check if a removal of 2 stones is allowed and give a correct prompt
    """
    if pile > 1:
        print(f'There are {pile} stones left')
        removal = 0
        if player == 1:
            removal = ai_turn(pile)
        else:
            removal = int(input(f'Player {player} would you like to remove 1 or 2 stones? '))
        while removal not in ACCEPTABLE_REMOVAL:
            removal = int(input('Please enter 1 or 2: '))
        print(f'Player {player} removes {removal} stone(s)\n')
        return pile - removal
    else:
        print(f'There is {pile} stone left')
        print(f'Player {player}, you remove 1 stone')
        return 0

def ai_turn(pile: int):
    best_move = (pile - 1) % 3
    if best_move == 0:
        return 0
    return best_move

def nimm()->None:
    """
    Runs the game loop as long as the pile is not 0
    I ended up having to use break
    There's probably a better way of doing this loop
    """
    pile = INITIAL_STONES
    while pile > 0:
        for player in range(1, PLAYER_COUNT + 1):
            pile = remove_stones(pile, player)
            if pile == 0:
                game_over(player)
                break
            
def ai_test():
    for i in range(20, 1, -1):
        print(i, ai_turn(i))

if __name__ == '__main__':
    #ai_test()
    main()