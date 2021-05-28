"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

def main():
    total: int = 0
    while True:
        new_number = get_number()
        if new_number == 0:
            break
        total += new_number
        print(f'Running total is {total}\n')


def get_number()->int:
    return int(input('Enter a value: '))

if __name__ == '__main__':
    main()