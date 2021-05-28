
ASTRO_MIN_HEIGHT = 1.6
ASTRO_MAX_HEIGHT = 1.9

def main():
    height = get_user_height()
    verify_height(height)

def get_user_height():
    return float(input('Enter your height in meters: '))

def verify_height(height):
    if height < ASTRO_MIN_HEIGHT:
        print('Below minimum astronaut height')
    elif height > ASTRO_MAX_HEIGHT:
        print('Above maximum astronaut height')
    else:
        print('Correct height to be an astronaut')

if __name__ == "__main__":
    main()