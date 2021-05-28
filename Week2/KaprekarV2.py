"""
Gives the Kaprekar sequence for a given number
That is the number in least-to-greatest order for its digits
subtracted from its greatest-to-least order for its digits
until the result is 6174, Kaprekar's constant
This number should be reached in at most 8 iterations

This implementation treats the numbers as strings to more easily sort
and add leading 0's as needed

Kaprekar's constant is mentioned in Q2 of Khansole, "Mad Libs"
"""

def main():
    str_number: str = get_starting_number_string()
    #number = int(input('Enter a 4-digit number with at least two different digits: '))
    i = 0
    while not (str_number == '6174' or str_number == '0000'):
        print(str_number)
        str_number = kaprekar_routine(str_number)
        i += 1
    print(str_number)
    print(f'In {i} iterations')

#Gets the starting number for the sequence
#Checks if the given number is actually a number of 4 digits
#Currently cannot check if the number has at least 2 different digits
def get_starting_number_string()->str:
    str_number = input('Enter a 4-digit number with at least two different digits: ')
    while not (str_number.isnumeric() and len(str_number) == 4):
        str_number = input('Enter a 4-digit number with at least two different digits: ')
    return str_number

#Runs an iteration of the Kaprekar sequence
def kaprekar_routine(str_number: str)->str:
    number = sorted_number(str_number)
    rev_number = reverse_number(str_number)
    if number > rev_number:
        new_number =  number - rev_number
        print(f'{number} - {rev_number} gives: ', end='')
    else:
        new_number =  rev_number - number
        print(f'{rev_number} - {number} gives: ', end='')
    return make_four_digits(new_number)

#Makes an integer of the number in greatest-to-least order of its digits
def sorted_number(str_number: str)->int:
    str_number = ''.join(sorted(str_number))[::-1]
    return int(str_number)

#Makes an integer of the number in least-to-greatest order of its digits
def reverse_number(str_number: str)->int:
    rev_number_str  = ''.join(sorted(str_number))
    return int(rev_number_str)

def make_four_digits(number: int)->str:
    str_number = str(number)
    number_length = len(str_number)
    for i in range(4 - number_length):
        str_number = '0' + str_number
    return str_number

if __name__ == '__main__':
    main()