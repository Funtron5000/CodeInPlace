
"""
>>> leap_check_1(2000)
True
"""

def main():
    year = int(input('Enter a year to check if it\'s a leap year: '))
    print(leap_check(year))

def leap_check_1(year: int)->bool:
    return year % 4 == 0
    #    return True
    #return False

def leap_check_2(year: int)->bool:
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    return True

def leap_check(year: int)->str:
    if leap_check_1(year) and leap_check_2(year):
        return 'That\'s a leap year!'
    return 'That\'s not a leap year!'

if __name__ == "__main__":
    main()