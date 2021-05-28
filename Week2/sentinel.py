"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

def main():
    total = 0
    number = 0
    while number != -1:
        total = total + number
        number = new_number()
    print('total is %d' %total)
        
def new_number()->int:
    return int(input('Type a number: '))

if __name__ == '__main__':
    main()