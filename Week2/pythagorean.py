import math

def main():
    length_ab = float(input('Enter the length of AB: '))
    length_ac = float(input('Enter the length of AC: '))
    hypotenuse = math.sqrt(length_ab**2 + length_ac**2)
    print(f'The length of BC (the hypotenuse) is: {hypotenuse}')

if __name__ == "__main__":
    main()