
MIN_HEIGHT = 50



def main():
    height_str = input('How tall are you? ')
    while height_str != "":
        height = int(height_str)
        tall_enough(height)
        height_str = input('How tall are you? ')
    print('Good-bye!')

def tall_enough(height: int)->None:
    if height >= MIN_HEIGHT:
        print('You\'re tall enough to ride!')
    else:
        print('You\'re not tall enough to ride!')

if __name__ == "__main__":
    main()