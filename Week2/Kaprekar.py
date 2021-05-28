"""
Gives the Kaprekar sequence for a given number
That is the number in least-to-greatest order for its digits
subtracted from its greatest-to-least order for its digits
until the result is 6174, Kaprekar's constant
This number should be reached in at most 8 iterations
Some numbers will reach 0 instead though

Kaprekar's constant is mentioned in Q2 of Khansole, "Mad Libs"
"""

def main():
    number = get_starting_number()
    #number = int(input('Enter a 4-digit number with at least two different digits: '))
    i = 0
    while not (number == 6174 or number == 0):
        print(number)
        number = kaprekar_routine(number)
        i += 1
    print(number)
    print(f'In {i} iterations')

#Gets the starting number for the sequence
#Checks if the given number is actually a number of 4 digits
#Currently cannot check if the number has at least 2 different digits
def get_starting_number()->int:
    str_number = input('Enter a 4-digit number with at least two different digits: ')
    while not (str_number.isnumeric() and len(str_number) == 4):
        str_number = input('Enter a 4-digit number with at least two different digits: ')
    return int(str_number)

#Runs an iteration of the Kaprekar sequence
def kaprekar_routine(number: int)->int:
    number = sorted_number(number)
    rev_number = reverse_number(number)
    if number > rev_number:
        return number - rev_number
    else:
        return rev_number - number

#Makes a string of the number in greatest-to-least order of its digits
def sorted_number(number: int)->int:
    str_number = ''.join(sorted(str(number)))[::-1]
    return int(str_number)

#Makes a string of the number in least-to-greatest order of its digits
def reverse_number(number: int)->int:
    rev_number_str  = ''.join(sorted(str(number)))
    return int(rev_number_str)

if __name__ == '__main__':
    main()