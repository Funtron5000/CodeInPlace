
DOG_YEARS = 7.18

def main():
    human_age = int(input('Enter an age in human years: '))
    dog_age = human_age * DOG_YEARS
    print(f'That\'s {dog_age} in dog years!')

if __name__ == "__main__":
    main()