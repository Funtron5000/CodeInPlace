def main():
    numerator = int(input('Please enter an integer to be divided: '))
    denominator = int(input('Please enter an integer to divide by: '))
    quotient = numerator // denominator
    remainder = numerator % denominator
    print(f'The result of this division is {quotient} with a remainder of {remainder}')

if __name__ == "__main__":
    main()