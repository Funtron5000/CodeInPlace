
RRRR = "33"
AFFIRMATION = "RAWR XD"

def main():
    while get_affirmation() != AFFIRMATION:
        print('That was not the affirmation.')
    print('That\'s right!')

def get_affirmation()->str:
    return input(f'Please type the following affirmation: {AFFIRMATION}\n')

if __name__ == "__main__":
    main()