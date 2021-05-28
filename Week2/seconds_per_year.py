
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

def main():
    #print(f'The number of hours in a year is {hours_per_year()}')
    #print(f'The number of minutes in a year is {minutes_per_year()}')
    print(f'The number of seconds in a year is {seconds_per_year()}')

def hours_per_year()->int:
    return DAYS_IN_YEAR * HOURS_IN_DAY

def minutes_per_year()->int:
    return hours_per_year() * MINUTES_IN_HOUR

def seconds_per_year()->int:
    return minutes_per_year() * SECONDS_IN_MINUTE

if __name__ == "__main__":
    main()