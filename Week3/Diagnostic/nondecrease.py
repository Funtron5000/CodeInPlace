def main():
    sequence = 0
    print('Enter a sequence of non-decreasing numbers.')
    number = float(input('Enter num: '))
    while True:
        sequence += 1
        number = get_new_number(number)
        if number == 'Bad':
            break
    print('Thanks for playing!')
    print(f'Sequence length: {sequence}')

def get_new_number(old_number):
    new_number = float(input('Enter num: '))
    if new_number > old_number:
        return new_number
    return 'Bad'

if __name__ == "__main__":
    main()