def main():
    animal = your_favorite_animal()
    agreement_animal(animal)

def your_favorite_animal()->str:
    animal = input('What\'s your favorite animal? ')
    return animal

def agreement_animal(animal: str)->None:
    print(f'My favorite animal is also {animal}!')

if __name__ == "__main__":
    main()