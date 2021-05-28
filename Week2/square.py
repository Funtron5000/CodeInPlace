def main():
    number = float(input('Type a number to see its square: '))
    number_squared = square(number)
    print(f'{number} squared is {number_squared}')

def square(number:float)->float:
    return number * number

if __name__ == "__main__":
    main()