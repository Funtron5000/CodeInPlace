"""
Plays the game, Nimm
A pile of stones exists and each player takes turns removing one or two stones
Whoever is last to take from the pile loses
The number of stones, players, and 
"""

import random
INITIAL_STONES = 3
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
        removal = 0
        #I ended up using a constant list here. I am not sure how to better check that the input is 1 or 2
        while removal not in ACCEPTABLE_REMOVAL:
            print(f'There are {pile} stones left')
            removal = int(input(f'Player {player} would you like to remove 1 or 2 stones? '))
        return pile - removal
    else:
        print(f'There is {pile} stone left')
        print(f'Player {player}, you remove 1 stone')
        return 0

def nimm()->None:
    """
    Runs the game loop as long as the pile is not 0
    I ended up having to use break
    There's probably a better way of doing this loop
    """
    pile = INITIAL_STONES
    while pile > 0:
        for player in range(PLAYER_COUNT):
            player += 1
            pile = remove_stones(pile, player)
            if pile == 0:
                game_over(player)
                break
            

if __name__ == '__main__':
    main()