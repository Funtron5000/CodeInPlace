"""
Gets an integer from the user and prints the hailstone sequence
"""

def main():
    number = int(input('Enter a number: '))
    run_hailstone(number)

#runs the hailstone sequence
def run_hailstone(number: int):
    while number != 1:
        if number % 2 == 0:
            number = even(number)
        else:
            number = odd(number)
    
#make 3n+1 of the number passed
def odd(number: int)->int:
    new_number = (3 * number) + 1
    print(f'{number} is odd, so I make 3n+1: {new_number}')
    return new_number

#take half of number passed
def even(number: int)->int:
    new_number = int(number / 2)
    print(f'{number} is even, so I take half: {new_number}')
    return new_number

if __name__ == '__main__':
    main()