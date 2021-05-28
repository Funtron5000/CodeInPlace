"""
Prints the Fizz Buzz sequence up to a given number.
Gets the number to count to from the user
"""
FIZZ_NUM = 3
BUZZ_NUM = 5

Fizz_Count = 0
Buzz_Count = 0
Fizzbuzz_Count = 0

def main():
    limit = get_limit()
    for i in range(1, limit):
        fizz_buzz(i)
    print(f'\nFizz count: {Fizz_Count}')
    print(f'Buzz count: {Buzz_Count}')
    print(f'Fizzbuzz count: {Fizzbuzz_Count}')
 
def get_limit()->int:
    return int(input('Number to count to: '))

def fizz_buzz(number: int)->None:
    global Fizz_Count
    global Buzz_Count
    global Fizzbuzz_Count

    if divisible(number, FIZZ_NUM) and divisible(number, BUZZ_NUM):
        print('Fizzbuzz')
        Fizzbuzz_Count += 1
    elif divisible(number, FIZZ_NUM):
        print('Fizz')
        Fizz_Count += 1
    elif divisible(number, BUZZ_NUM):
        print('Buzz')
        Buzz_Count += 1
    else:
        print(f'{number}')

def divisible(numerator: int, denominator: int)->bool:
    if numerator % denominator == 0:
        return True
    return False

if __name__ == '__main__':
    main()